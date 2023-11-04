<template>
  <div class="container mx-auto py-4">
    <div class="flex justify-between">
      <div class="flex gap-3">
        <IconNews />
        <p class="font-medium">{{ PRODUCT_NAME }}</p>
      </div>

      <div class="flex gap-4">
        <a :href="BACKEND_LOGIN_AUTH">Login</a>
        <a :href="BACKEND_SIGNUP_AUTH">Signup</a>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { IconNews } from "@tabler/icons-vue";
import {
  BACKEND_LOGIN_AUTH,
  BACKEND_SIGNUP_AUTH,
  PRODUCT_NAME,
} from "@/constants";
</script>
