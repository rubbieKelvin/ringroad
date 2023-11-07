<template>
  <div class="h-full flex items-center justify-center">
    <div class="min-w-[30em] flex gap-6 flex-col">
      <div class="flex gap-2 items-center">
        <IconBuildingStore :size="32" />
        <h1 class="text-2xl flex-grow">Select store</h1>
        <RouterLink
          class="bg-black text-white px-4 py-2 rounded-md"
          :to="{ name: 'create-store' }"
        >
          Create
        </RouterLink>
      </div>

      <div
        class="flex gap-1 items-center bg-black bg-opacity-10 rounded-md p-2"
      >
        <IconInfoSmall />
        <span class="text-sm"> You dont have any stores in your account </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useUserStore } from "@/store/user";
import { IconBuildingStore, IconInfoSmall } from "@tabler/icons-vue";
import { RouterLink } from "vue-router";

const { getUser } = useUserStore();
getUser();
</script>
