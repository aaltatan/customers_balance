<script>
  import { Link } from "svelte-routing";
  import { fade } from "svelte/transition";
  import { parseDate } from "../utils/functions";
  import { _ } from 'svelte-i18n'
  import ContextMenu from "./ContextMenu.svelte";
  import Clock from "../components/icons/Clock.svelte";
  
  export let customer;
  export let ratio = "1.5rem";

  const cls = (amount = 0) => {
    return amount > 0 ? "text-orange-600" : "text-green-600";
  };
</script>

<div class="rounded-md shadow-sm md:p-2 duration-150 hover:shadow-md" in:fade>
  <header class="pt-2 px-2 flex items-center">
    <h2 class="text-lg">
      <Link
        class="focus:ring-2 ring-orange-500 outline-none focus:p-1 rounded-md duration-150 hover:underline"
        tabindex="0 "
        to={"/ledger/" + customer.customer__id}
      >
        {customer.customer__name}
      </Link>
      <div class="flex items-center gap-1 text-xs text-slate-400 font-semibold">
        <span>
          <Clock ratio=".75rem" />
        </span>
        {parseDate(customer.last_date)}
        <span>
          ({customer.transactions_count})
        </span>
      </div>
    </h2>
    <div class="relative ltr:ml-auto rtl:mr-auto">
      <ContextMenu {ratio}>
        <li>
          <Link class="p-2 block w-full text-center" to={`/ledger/${customer.customer__id}`}>
            {$_('components.customerCard.contextMenu.ledger')}
          </Link>
        </li>
        <li>
          <Link class="p-2 block w-full text-center" to={`/add-debit/${customer.customer__id}`}>
            {$_('components.customerCard.contextMenu.addDebit')}
          </Link>
        </li>
        <li>
          <Link class="p-2 block w-full text-center" to={`/add-credit/${customer.customer__id}`}>
            {$_('components.customerCard.contextMenu.addCredit')}
          </Link>
        </li>
      </ContextMenu>
    </div>
  </header>
  <div class={`p-2 md:font-semibold ${cls(customer.customer_net)}`}>
    {customer.customer_net.toLocaleString()}
  </div>
</div>
