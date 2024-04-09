<script>
  import { Link } from "svelte-routing";
  import { breadcrumb } from "../stores/store";
</script>

<div class="flex items-center gap-1 tracking-tighter select-none">
  {#if $breadcrumb}
    {#each $breadcrumb as b, idx (b.to)}
      {#if idx + 1 === $breadcrumb.length && $breadcrumb.length > 1}
        <span>&gt;</span>
        <span>{b.text}</span>
      {:else}
        <Link class="text-orange-500 underline block" to={b.to}>
          {b.text}
        </Link>
      {/if}
    {/each}
  {/if}
</div>
