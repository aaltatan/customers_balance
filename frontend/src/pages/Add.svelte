<script>
  import { scale, slide } from "svelte/transition";
  import AddCustomer from "../components/AddCustomer.svelte";
  import AddTransaction from "../components/AddTransaction.svelte";
  import { _ } from 'svelte-i18n';

  export let id = null;
  export let type = null;

  let activeTab = AddTransaction;
</script>

<div in:scale={(0, 200)}>
  <div>
    <button
      class={`duration-150 relative rounded-tr-2xl rounded-tl-lg py-2 px-4 border border-slate-50 outline-orange-500  z-10 tracking-tighter ${activeTab === AddTransaction ? "bg-white translate-y-[1px] border-b-white hover:bg-white font-semibold" : "bg-slate-50 hover:bg-slate-100"}`}
      on:click={() => (activeTab = AddTransaction)}
    >
      {$_('pages.addTransaction.tabs.addTransaction')}
    </button>
    <button
      class={`duration-150 relative rounded-tr-2xl rounded-tl-lg py-2 px-4 border border-slate-50 outline-orange-500  z-10 tracking-tighter ${activeTab === AddCustomer ? "bg-white translate-y-[1px] border-b-white hover:!bg-white font-semibold" : "bg-slate-50 hover:bg-slate-100"}`}
      on:click={() => (activeTab = AddCustomer)}
    >
    {$_('pages.addTransaction.tabs.addCustomer')}
    </button>
  </div>
  <div
    class="rounded-br-lg rounded-bl-lg rounded-tr-lg px-4 py-12 border border-slate-50 shadow-sm"
  >
    {#if activeTab === AddTransaction}
      <svelte:component this={activeTab} {id} {type} />
    {:else}
      <svelte:component this={activeTab} />
    {/if}
  </div>
</div>
