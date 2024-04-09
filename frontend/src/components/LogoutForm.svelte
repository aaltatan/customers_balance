<script>
  import { getCookie } from "../utils/functions";
  import Logout from "../components/icons/Logout.svelte";
  import { _ } from "svelte-i18n";

  const csrftoken = getCookie("csrftoken");

  export let ratio;
</script>

<form action="/accounts/logout/" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
  <button class="cir-hover !flex items-center gap-2 !p-2" type="submit" title={$_("logout")}>
    <Logout {ratio} />
    {$_("logout")}
  </button>
</form>
