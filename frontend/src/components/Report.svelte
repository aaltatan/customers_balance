<script>
  import { _ } from "svelte-i18n";
  export let report;
</script>

<div class="mb-4">
  {#if report}
    <div
      class="flex items-center gap-2 overflow-x-auto overflow-hidden p-3 font-semibold text-sm md:text-lg max-md:shadow-inner rounded-md max-md:bg-slate-50"
    >
      <span class="p-2 bg-white block min-w-32 w-full md:p-3 rounded-md whitespace-nowrap border border-slate-50">
        {$_("components.report.net")}:<br />
        {report.net ? report.net.toLocaleString() : 0}
      </span>
      <span class="p-2 bg-white block min-w-32 w-full md:p-3 rounded-md whitespace-nowrap border border-slate-50">
        {$_("components.report.transactionsCount")}:<br />
        {report.transactions_count ? report.transactions_count.toLocaleString() : 0}
      </span>
      <span class="p-2 bg-white block min-w-32 w-full md:p-3 rounded-md whitespace-nowrap border border-slate-50">
        {$_("components.report.customersCount")}:<br />
        {report.customers_count ? report.customers_count.toLocaleString() : 0}
      </span>
      <span class="text-orange-600 p-2 bg-white block min-w-32 w-full md:p-3 rounded-md whitespace-nowrap border border-slate-50">
        {$_("components.report.totalDebit")}:<br />
        {report.total_debit ? report.total_debit.toLocaleString() : 0}
      </span>
      <span class="text-green-600 p-2 bg-white block min-w-32 w-full md:p-3 rounded-md whitespace-nowrap border border-slate-50">
        {$_("components.report.totalCredit")}:<br />
        {report.total_credit ? report.total_credit.toLocaleString() : 0}
      </span>
    </div>
  {/if}
</div>
