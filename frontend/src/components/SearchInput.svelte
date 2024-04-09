<script>
  import Search from "./icons/Search.svelte";
  import Loading from "./icons/Loading.svelte";
  import { createEventDispatcher, onDestroy, onMount } from "svelte";
  import axios from "axios";
  import { _ } from "svelte-i18n";
  import { getCookie } from "../utils/functions";

  export let id;

  const dispatch = createEventDispatcher();
  const csrftoken = getCookie("csrftoken");

  $: searchResults = null;
  let keyword;
  let timeout;
  let customerName = "";
  let closed = false;
  let loading = false;
  let searchRef;

  const getCustomerById = async (id) => {
    const response = await axios.get("/api/customers/" + id);
    return response.data;
  };

  const spanCloseHandler = () => {
    customerName = "";
    keyword = "";
    dispatch("search", "");
  };

  const onBodyClick = () => {
    closed = true;
    keyword = "";
  };

  const addCustomer = async (e, customerName) => {
    loading = true;
    const response = await fetch("/api/customers/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ name: customerName }),
    });
    const data = await response.json();
    customerSelectHandler(e, data);
    loading = false;
  };

  const customerSelectHandler = (e, result) => {
    customerName = result.name;
    searchResults = null;
    keyword = "";
    dispatch("search", result);
  };

  const searchHandler = (e, keyword) => {
    closed = false;
    clearTimeout(timeout);
    if (keyword && keyword.trim()) {
      loading = true;
      timeout = setTimeout(async () => {
        e.preventDefault();
        const response = await fetch(`/api/customers/search/${keyword}`);
        const results = await response.json();
        searchResults = results;
        loading = false;
      }, 500);
    } else {
      searchResults = null;
    }
  };

  document.body.addEventListener("click", onBodyClick);
  onDestroy(() => {
    document.body.removeEventListener("click", onBodyClick);
  });

  onMount(async () => {
    if (id) {
      let cus = await getCustomerById(id);
      customerSelectHandler(null, cus);
    } else {
      searchRef.focus();
    }
  });
</script>

<div class="relative">
  {#if customerName}
    <div
      class="absolute ltr:left-10 rtl:right-10 top-1/2 -translate-y-1/2 bg-orange-600 text-white rounded-md px-2 font-semibold"
    >
      <span>{customerName}</span>
      {#if !id}
        <span
          class="text-lg cursor-pointer"
          on:click={spanCloseHandler}
          on:keyup={spanCloseHandler}
        >
          ×
        </span>
      {/if}
    </div>
  {/if}

  <span class="absolute ltr:left-2 rtl:right-2 top-1/2 -translate-y-1/2">
    <Search ratio="1.5rem" />
  </span>

  {#if loading}
    <span class="absolute ltr:right-10 rtl:left-10 top-1/2 -translate-y-1/2">
      <Loading ratio="1.5rem" />
    </span>
  {/if}

  <input
    class="bg-slate-50 shadow-inner focus:ring-2 ring-orange-500 rounded-md py-3 ltr:pl-10 rtl:pr-10 ltr:pr-4 rtl:pl-4 outline-0 block w-full disabled:bg-slate-100"
    type="search"
    disabled={customerName ? "disabled" : ""}
    placeholder={$_("components.searchInput.placeholder")}
    bind:this={searchRef}
    bind:value={keyword}
    on:keyup={(e) => searchHandler(e, keyword)}
    on:search={(e) => searchHandler(e, keyword)}
  />

  {#if searchResults && !closed}
    <ul
      class="absolute bg-white top-[calc(100%+4px)] left-0 rounded-md divide-y divide-slate-100 z-10 w-full shadow-sm overflow-x-hidden overflow-y-auto max-h-32"
    >
      {#each searchResults as result, idx (result.id)}
        <li>
          <button
            on:click={(e) => customerSelectHandler(e, result)}
            class="py-2 text-left px-4 tracking-tighter font-semibold w-full hover:bg-slate-100 focus:bg-slate-200 outline-none"
          >
            {result.name}
          </button>
        </li>
      {:else}
        <li
          class="py-2 text-left px-4 tracking-tighter font-semibold w-full outline-none flex items-center flex-wrap gap-2"
        >
          <span
            ><span class="underline">{keyword}</span>
            {$_("components.searchInput.notExistsMessage")}</span
          >
          <button class="btn btn-primary py-1 px-2" on:click={(e) => addCustomer(e, keyword)}>
            {$_("components.searchInput.add")} <span class="underline">{keyword}</span>
          </button>
        </li>
      {/each}
    </ul>
  {/if}
</div>
