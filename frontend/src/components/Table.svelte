<script>
  import { slide } from "svelte/transition";

  export let headers;
</script>

<div 
class="overflow-x-auto rounded-md shadow-inner"
in:slide={0, 300}
>
  <table class="report table-auto w-full text-nowrap">
    <thead>
      <tr class="capitalize bg-slate-400 text-white ltr:text-left rtl:text-right">
        <th>#</th>
        {#each headers as header }
          <th>{header}</th>
        {/each}
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-100">
      <slot />
    </tbody>
  </table>
</div>