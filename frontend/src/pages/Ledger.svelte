<script>
  import { onMount } from "svelte";
  import LoadingModal from "../components/LoadingModal.svelte";
  import { parseDate } from "../utils/functions.js";
  import { breadcrumb } from "../stores/store";
  import { Link } from "svelte-routing";
  import Table from "../components/Table.svelte";
  import { _ } from 'svelte-i18n';
  

  export let id;
  let ledgerData;
  let customerName;
  let headers = [
    $_('pages.ledger.tableHeader.amount'),
    $_('pages.ledger.tableHeader.net'),
    $_('pages.ledger.tableHeader.date'),
    $_('pages.ledger.tableHeader.user'),
  ];

  const cls = (amount = 0) => {
    return amount > 0 ? "text-orange-600" : "text-green-600";
  };

  const getLedger = async (id) => {
    const response = await fetch("/api/transactions/ledger/" + id);
    const data = await response.json();
    ledgerData = data;
    customerName = data.at(0).customer.name;
  };

  onMount(async () => {
    await getLedger(id);
    document.title = customerName;
    breadcrumb.set([
      { to: "/", text: $_('pages.ledger.home') },
      { to: `/ledger/${id}`, text: customerName },
    ]);
  });
</script>

{#if ledgerData}
  <Table {headers}>
    {#each ledgerData as t, idx (t.id)}
      <tr>
        <td>{idx + 1}</td>
        <td>
          <span class={`${cls(t.amount)}`}>{t.amount.toLocaleString()}</span>
        </td>
        <td>{t.running_net.toLocaleString()}</td>
        <td>{parseDate(t.date)}</td>
        <td>{t.user.username}</td>
      </tr>
    {/each}
  </Table>
  <div class="flex items-center justify-center gap-1 my-4">
    <Link to={`/add-debit/${id}`} class="btn btn-primary px-2 py-1">
      {$_('pages.ledger.btns.debit')}
    </Link>
    <Link to={`/add-credit/${id}`} class="btn btn-success px-2 py-1">
      {$_('pages.ledger.btns.credit')}
    </Link>
  </div>
{:else}
  <LoadingModal />
{/if}
