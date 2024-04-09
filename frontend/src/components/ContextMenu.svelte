<script>
  import Ellipsis from "./icons/Ellipsis.svelte";
  export let ratio = "1.5rem";
  export let top = "top-0";
  export let start = true;

</script>

<!-- svelte-ignore a11y-positive-tabindex -->
<span
  role="button"
  tabindex="1"
  class="peer/btn block cir-hover"
  on:click={() => (open = true)}
  on:keydown={() => (open = true)}
>
  <Ellipsis {ratio} />
</span>

{#if open}
  <ul
    class={`context-menu scale-0 hover:scale-100 peer-hover/btn:scale-100 rtl:origin-top-left ltr:origin-top-right absolute ${start ? "ltr:right-full rtl:left-full" : "ltr:right-0 rtl:left-0"} ${top} bg-white rounded-md shadow-lg divide-y divide-slate-200 overflow-hidden duration-150 delay-75 w-28 sm:w-32 sm:text-sm md:text-sm border border-slate-200 z-10`}
  >
    <slot />
  </ul>
{/if}
