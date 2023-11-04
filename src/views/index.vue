<template>
  <!-- <div class="flex items-center justify-center">
    <div class="border border-gray-300 flex rounded-md gap-4 flex-col p-4">
      <h1 class="font-medium text-2xl">Inventory manager</h1>
      <p>Manage your store's inventory</p>
      <div class="flex gap-2">
        <a :href="BACKEND_SIGNUP_AUTH" class="btn bg-gray-500 text-white"
          >Sign Up</a
        >
        <a :href="BACKEND_LOGIN_AUTH" class="btn border border-gray-300">
          Sign In
        </a>
      </div>
    </div>
  </div> -->
  <div class="h-full flex flex-col">
    <NavBar />
    <div class="container mx-auto flex-grow items-center flex">
      <div class="flex flex-col gap-6 pl-4">
        <h1 class="font-bold text-3xl max-w-[16em]">
          Streamline Your Inventory Management with {{ PRODUCT_NAME }}
        </h1>

        <p class="max-w-[30em] text-gray-800">
          Welcome to {{ PRODUCT_NAME }}, where we make inventory management a
          breeze. Say goodbye to inventory-related headaches and hello to
          organized, efficient, and cost-effective inventory control.
        </p>

        <a
          :href="BACKEND_SIGNUP_AUTH"
          class="bg-black text-white px-5 py-3 rounded-md w-max hover:bg-gray-700">
          Get Started
        </a>
      </div>
    </div>
    <NavFooter/>
  </div>
</template>

<style lang="scss">
.btn {
  @apply rounded-md flex-grow py-2 text-center;
}
</style>

<script lang="ts" setup>
import NavBar from "@/components/NavBar.vue";
import NavFooter from "@/components/NavFooter.vue";
import { BACKEND_SIGNUP_AUTH, PRODUCT_NAME } from "@/constants";
</script>
