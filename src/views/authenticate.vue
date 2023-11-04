<template>
  <div class="flex flex-col items-center justify-center">
    <div class="flex items-center gap-5">
      <svg
        class="animate-spin h-5 w-5 text-gray-500"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
      >
        <circle
          class="opacity-25"
          cx="12"
          cy="12"
          r="10"
          stroke="currentColor"
          stroke-width="4"
        ></circle>
        <path
          class="opacity-75"
          fill="currentColor"
          d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
        ></path>
      </svg>

      <div>
        <h1 class="font-medium">Authenticating</h1>
        <p class="text-sm">Verifying authentication, this wont be long...</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRoute } from "vue-router";
import { BACKEND_SIGNUP_AUTH } from "@/constants";
import { onMounted } from "vue";

const route = useRoute();
const { code, user } = route.query;

onMounted(() => {
  if (!(code && user)) {
    const url = new URL(BACKEND_SIGNUP_AUTH);
    url.searchParams.set("flash", "Error, could'nt derive user, Try signing in");
    window.open(url, '_self');
  }
});
</script>
