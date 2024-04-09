<script>
  import { onMount, getContext } from 'svelte';
  import ContextMenu from '../components/ContextMenu.svelte'
  import LogoutForm from "./LogoutForm.svelte";
  import LanguageToggle from "./LanguageToggle.svelte";

  let user = getContext('username');

</script>

<div class="flex items-center gap-1 rounded-md bg-slate-50 hover:bg-slate-100 px-2 py-1 relative duration-150">
  <span class='font-semibold'>{user}</span>
  <ContextMenu ratio="1.25rem" top="top-full" start={false}>
    <li>
      <LanguageToggle />
    </li>
    <li>
      <LogoutForm ratio="1.25rem" />
    </li>
  </ContextMenu>

</div>