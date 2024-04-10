<script>
  import FlashMessages from "../components/FlashMessages.svelte";
  import CustomerCard from "../components/CustomerCard.svelte";
  import LoadingModal from "../components/LoadingModal.svelte";
  import Loading from "../components/icons/Loading.svelte";
  import Plus from "../components/icons/Plus.svelte";
  import Report from "../components/Report.svelte";
  import ExportExcel from "../components/ExportExcel.svelte";
  import { onMount } from "svelte";
  import { Link } from "svelte-routing";
  import { breadcrumb } from "../stores/store";
  import { slide } from "svelte/transition";
  import { _ } from "svelte-i18n";
  import axios from "axios";

  let customers;
  let report;
  let keyword = "";
  let searchTimeout;
  let loading = false;
  let order_by;
  let show_all;

  const fetchReport = async () => {
    try {
      const response = await axios.get("/api/transactions/report");
      report = response.data;
      if (response.status === 401) {
        location.reload();
      }
    } catch (error) {
      console.log(error);
    }
  };

  const searchHandler = (e, duration) => {
    loading = true;
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      fetchBalance();
    }, duration);
  };

  const fetchBalance = async () => {
    let query = new URLSearchParams();
    query.append("keyword", keyword);
    query.append("order_by", order_by);
    query.append("show_all", show_all);
    const endpoint = `/api/transactions/balance?${query.toString()}`;
    const response = await fetch(endpoint);
    const data = await response.json();
    customers = data;
    loading = false;
  };

  onMount(() => {
    order_by = localStorage.getItem("order_by") || "customer__name";
    show_all = +localStorage.getItem("show_all") || 0;
    fetchBalance();
    fetchReport();
    document.title = $_("pages.home.documentTitle");
    breadcrumb.set([{ to: "/", text: $_("pages.home.documentTitle") }]);
  });
</script>

<FlashMessages />

<div class="fixed bottom-4 rtl:left-4 ltr:right-4 flex gap-1 z-20 items-center">
  <Link class="btn btn-primary !rounded-full text-xl p-1  shadow-md" to="/add">
    <Plus ratio="2.5rem" />
  </Link>
</div>

<Report {report} />

<div>
  <label class="font-semibold tracking-tighter text-sm block py-1" for="ordering-selection">
    {$_("pages.home.orderBy")}:
  </label>
  <select
    bind:value={order_by}
    on:change={() => {
      localStorage.setItem("order_by", order_by);
      fetchBalance();
    }}
    id="ordering-selection"
    class="py-1 px-2 bg-orange-500 text-white font-semibold rounded-md outline-none focus:ring-2 ring-orange-600"
  >
    <option class="bg-white text-black py-1 font-semibold" value="customer__name"
      >{$_("pages.home.orderOptions.az")}</option
    >
    <option class="bg-white text-black py-1 font-semibold" value="-customer__name"
      >{$_("pages.home.orderOptions.za")}</option
    >
    <option class="bg-white text-black py-1 font-semibold" value="-customer_net"
      >{$_("pages.home.orderOptions.gs")}</option
    >
    <option class="bg-white text-black py-1 font-semibold" value="customer_net"
      >{$_("pages.home.orderOptions.sg")}</option
    >
    <option class="bg-white text-black py-1 font-semibold" value="last_date"
      >{$_("pages.home.orderOptions.on")}</option
    >
    <option class="bg-white text-black py-1 font-semibold" value="-last_date"
      >{$_("pages.home.orderOptions.no")}</option
    >
  </select>
</div>

<div class="flex items-center gap-1 mt-2">
  <button
    on:click={() => {
      show_all = show_all === 1 ? 0 : 1;
      localStorage.setItem("show_all", show_all);
      fetchBalance();
    }}
    class={`${!show_all ? "bg-orange-500 hover:!bg-orange-600" : "bg-orange-800 hover:!bg-orange-900"} text-white font-semibold  rounded-md block outline-none focus:ring-2 ring-orange-600 py-1 px-3 duration-150`}
  >
    <span>{!show_all ? $_("pages.home.showBtn.show") : $_("pages.home.showBtn.hide")}</span>
    <span>{$_("pages.home.showBtn.closedAccount")}</span>
  </button>

  <ExportExcel endpoint="/api/customers/excel" />
</div>

<div class="relative">
  <input
    type="search"
    bind:value={keyword}
    on:keyup={(e) => searchHandler(e, 500)}
    on:search={(e) => searchHandler(e, 0)}
    placeholder={$_("pages.home.search.placeholder")}
    class="bg-slate-50 ring-orange-500 focus:ring-2 rounded-md py-2 px-4 shadow-inner outline-none w-full block my-4"
  />
  {#if loading}
    <span class="absolute top-1/2 ltr:right-10 rtl:left-10 -translate-y-1/2">
      <Loading ratio="1.5rem" />
    </span>
  {/if}
</div>

<div>
  {#if customers}
    {#if customers.length}
      <div class="grid grid-cols-1 md:grid-cols-3 gap-2 duration-150" in:slide>
        {#each customers as customer (customer)}
          <CustomerCard {customer} />
        {/each}
      </div>
    {:else}
      <p class="capitalize tracking-tighter font-semibold">
        {$_("pages.home.search.noResults")}
      </p>
    {/if}
  {:else}
    <LoadingModal />
  {/if}
</div>
