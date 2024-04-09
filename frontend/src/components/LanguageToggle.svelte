<script>
  import { onMount } from "svelte";
  import Language from "./icons/Language.svelte";
  import { locale, _ } from "svelte-i18n";
  import { navigate } from "svelte-routing";

  const langToggler = () => {
    $locale = $locale === "ar" ? "en" : "ar";
    localStorage.setItem("lang", $locale);
    document.getElementById("app").setAttribute("dir", $locale === "ar" ? "rtl" : "ltr");
    let goTo = location.pathname === '/' ? '/home' : '/';
    navigate(goTo);
  };

  onMount(() => {
    $locale = localStorage.getItem("lang") || "ar";
    document.getElementById("app").setAttribute("dir", $locale === "ar" ? "rtl" : "ltr");
  });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<span
  on:click={langToggler}
  class="cir-hover !flex items-center gap-2 !p-2"
  title={$_("currentlanguage")}
>
  <Language ratio="1.25rem" />
  {$_("currentlanguage")}
</span>
