<script>
  import { _ } from 'svelte-i18n';

  export let value;
  export let label = 'debit';

  $: displayType = label === 'debit' ? 
    $_('pages.addTransaction.displayType.debit'): 
    $_('pages.addTransaction.displayType.credit');

</script>

<div class="relative">
  <label
    class="absolute top-1 ltr:left-4 rtl:right-4 text-sm text-slate-700 font-semibold tracking-tighter"
    for={displayType.toLowerCase()}>
      {displayType[0].toUpperCase() + displayType.substring(1, displayType.length).toLowerCase()}
    </label>
  <input
    class="bg-slate-50 focus:ring-2 rounded-md px-4 pt-6 pb-2 pr-4 outline-0 block w-full disabled:bg-slate-100 shadow-inner ring-orange-500 text-orange-600 font-semibold"
    type="number"
    id={displayType.toLowerCase()}
    min="0"
    bind:value={value}
    on:focus={(e) => e.target.select()}
  />
</div>
