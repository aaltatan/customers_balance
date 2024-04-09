<script>
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
  import { _ } from "svelte-i18n";
  import { getCookie } from "../utils/functions";

  const csrftoken = getCookie("csrftoken");
  let inputRef;
  let canSend = false;
  let inputName;
  let writeTimeout;
  let errorMessage;

  const fetchName = async () => {
    const response = await fetch("/api/customers/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({
        name: inputName,
      }),
    });
    try {
      if (response.status === 204) {
        canSend = true;
      } else if (response.status === 409) {
        errorMessage = $_('pages.addTransaction.addCustomerErrorMessage');
      }
    } catch (error) {
      console.log(error);
    }
  };

  const addCustomer = async (e, customerName) => {
    const response = await fetch("/api/customers/add", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name: customerName }),
    });
    if (response.status === 200) {
      inputName = "";
      errorMessage = null;
    }
  };

  const checkHandler = () => {
    errorMessage = null;
    if (inputName) {
      clearTimeout(writeTimeout);
      writeTimeout = setTimeout(() => {
        fetchName();
      }, 500);
    } else {
      canSend = false;
    }
  };

  onMount(() => {
    inputRef.focus();
  });
</script>

<div>
  <input
    class="bg-slate-50 shadow-inner focus:ring-2 ring-orange-500 rounded-md py-3 px-4 outline-0 block w-full disabled:bg-slate-100"
    type="text"
    placeholder={$_("pages.addTransaction.tabs.customerNamePlaceholder")}
    bind:this={inputRef}
    bind:value={inputName}
    on:keydown={checkHandler}
    in:fade
  />
</div>

{#if errorMessage}
  <p in:fade class="text-[red] font-semibold mt-2">{errorMessage}</p>
{/if}

<button
  disabled={canSend && inputName ? "" : "disabled"}
  class="btn btn-primary disabled:bg-orange-300 disabled:cursor-no-drop p-4 mt-4 w-full"
  on:click={(e) => addCustomer(e, inputName)}
>
  {$_("pages.addTransaction.add")}
</button>
