<script>
  import { onMount } from "svelte";

  let inputRef;

  onMount(() => {
    inputRef.focus();
  })
</script>

<input type="text" class="bg-orange-500" bind:this={inputRef}>