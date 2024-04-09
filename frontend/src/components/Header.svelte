<script>
  import Breadcrumb from "./Breadcrumb.svelte";
  import Records from "./icons/Records.svelte";
  import { Link } from "svelte-routing";
  import UserDropDown from "./UserDropDown.svelte";
  import { _ } from "svelte-i18n";
</script>

<header class="sticky top-4 left-0 bg-white p-4 rounded-lg shadow-md z-20">
  <nav class="flex items-center gap-1">
    <Breadcrumb />
    <div class="relative ltr:ml-auto rtl:mr-auto">
      <ul class="flex items-center gap-1 sm:gap-2 md:gap-4">
        <li>
          <Link
            class="cir-hover"
            to="/transactions"
            title={$_("pages.transactions.breadcrumb.transactions")}
          >
            <Records ratio="1.5rem" />
          </Link>
        </li>
        <li>
          <UserDropDown />
        </li>
      </ul>
    </div>
  </nav>
</header>
