<script>
  import { onMount } from "svelte";
  import { parseDate } from "../utils/functions.js";
  import LoadingModal from "../components/LoadingModal.svelte";
  import { Link } from "svelte-routing";
  import Loading from "../components/icons/Loading.svelte";
  import { breadcrumb } from "../stores/store";
  import Table from "../components/Table.svelte";
  import { _ } from "svelte-i18n";
  import ExcelExport from '../components/ExportExcel.svelte';

  let headers = [
    $_("pages.transactions.tableHeader.amount"),
    $_("pages.transactions.tableHeader.net"),
    $_("pages.transactions.tableHeader.customer"),
    $_("pages.transactions.tableHeader.date"),
    $_("pages.transactions.tableHeader.user"),
  ];

  const LIMIT = 10;
  let transactions;
  let limit = 10;
  let offset = 0;
  let lengthOfData = 0;
  let loading = false;

  const cls = (amount = 0) => {
    return amount > 0 ? "text-orange-600" : "text-green-600";
  };

  const fetchMore = () => {
    limit += LIMIT;
    fetchBalance(limit, offset);
  };

  const fetchBalance = async (limit, offset) => {
    loading = true;

    const query = `/api/transactions?limit=${limit}&offset=${offset}`;
    const response = await fetch(query);

    const data = await response.json();
    transactions = await data.items;
    lengthOfData = data.count;

    loading = false;
  };

  onMount(() => {
    document.title = $_("pages.transactions.breadcrumb.transactions");
    breadcrumb.set([
      { to: "/", text: $_("pages.transactions.breadcrumb.home") },
      { to: "/transactions", text: $_("pages.transactions.breadcrumb.transactions") },
    ]);
    fetchBalance(limit, offset);
  });
</script>

<div class="mb-8">
  {#if transactions}
    <Table {headers}>
      {#each transactions as t, idx (t)}
        <tr>
          <td>{idx + 1}</td>
          <td>
            <span class={`${cls(t.amount)}`}>
              {t.amount.toLocaleString()}
            </span>
          </td>
          <td>{t.running_net.toLocaleString()}</td>
          <td>
            <Link class="hover:underline" to={"/ledger/" + t.customer.id}>
              {t.customer.name}
            </Link>
          </td>
          <td>{parseDate(t.date)}</td>
          <td>{t.user.username}</td>
        </tr>
      {/each}
    </Table>
    <span class="text-slate-500 text-sm p-2 my-2 block">
      <span class="font-semibold">{transactions.length}</span>
      {$_("pages.transactions.tableMessage.of")}
      <span class="font-semibold">{lengthOfData}</span>
      {$_("pages.transactions.tableMessage.recordsFound")}
    </span>

    <div class="flex items-center justify-center gap-1">
      {#if lengthOfData > transactions.length}
        <button class="btn btn-primary py-2 px-3" on:click={fetchMore}>
          <div class="flex items-center gap-1">
            <span>
              {$_("pages.transactions.getMore")}
            </span>
            {#if loading}
              <Loading ratio="1rem" />
            {/if}
          </div>
        </button>
      {/if}
      <ExcelExport endpoint="/api/transactions/excel" />
    </div>
  {:else}
    <LoadingModal />
  {/if}
</div>
