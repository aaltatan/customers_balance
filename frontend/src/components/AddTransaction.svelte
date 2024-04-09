<script>
  import SearchInput from "./SearchInput.svelte";
  import NumberInput from "./NumberInput.svelte";
  import { navigate } from "svelte-routing";
  import axios from "axios";
  import { breadcrumb } from "../stores/store";
  import { onMount } from "svelte";
  import { _ } from "svelte-i18n";
  import { fade } from "svelte/transition";
  import { getCookie } from "../utils/functions";

  export let id = null;
  export let type = null;

  $: displayType =
    type === "debit"
      ? $_("pages.addTransaction.displayType.debit")
      : $_("pages.addTransaction.displayType.credit");

  const csrftoken = getCookie("csrftoken");
  let customer;
  let amount = 0;
  let errors;
  let searchRef;

  onMount(() => {
    breadcrumb.set([
      { to: "/", text: $_("pages.addTransaction.breadcrumb.home") },
      { to: "/add", text: `${displayType} ${$_("pages.addTransaction.breadcrumb.new")}` },
    ]);
    document.title = id
      ? `${$_("pages.addTransaction.breadcrumb.new")} ${displayType}`
      : $_("pages.addTransaction.documentTitle");
  });

  $: data = {
    type: type,
    amount: amount,
    customer: customer,
  };

  $: canSend = amount && customer;

  const addTransaction = async () => {
    try {
      await axios.post("/api/transactions/add", data, {
        headers: {
          "X-CSRFToken": csrftoken,
        },
      });
      navigate("/");
    } catch (e) {
      const errorsList = e.response.data.detail;
      errors = errorsList.map((error) => {
        const field = error.loc.at(-1);
        const message = error.msg;
        return `${field} ${message}`;
      });
    }
  };
</script>

<div class="flex flex-col gap-2" in:fade>
  <SearchInput
    bind:this={searchRef}
    {id}
    on:search={(e) => {
      customer = e.detail.id;
      if (type === "credit") {
        amount = Math.abs(e.detail.net);
      }
    }}
  />
  <NumberInput bind:value={amount} label={type} />
  {#if errors}
    <ul>
      {#each errors as error (error)}
        <li
          class="text-red-900 bg-red-200 px-4 py-2 rounded-md tracking-tighter font-semibold my-1"
        >
          {error}
        </li>
      {/each}
    </ul>
  {/if}
  <button
    class={`btn btn-${type === "credit" ? "success" : "primary"} ${type === "debit" ? "disabled:bg-orange-300" : "disabled:bg-green-300"} disabled:cursor-no-drop p-4 mt-4`}
    on:click={addTransaction}
    disabled={canSend ? "" : "disabled"}
  >
    {$_("pages.addTransaction.add")}
  </button>
</div>
