<script>
  import { onMount } from "svelte";
  import { getMessages } from "../utils/functions";
  import { fade } from "svelte/transition";

  let flashMessages;

  onMount(async () => {
    flashMessages = await getMessages();
  })
</script>

{#if flashMessages}
  <div 
  in:fade
  class="bg-green-600 font-semibold tracking-tighter text-white px-4 py-2 rounded-md my-4"
  >
    {flashMessages}
  </div>
{/if}
