<template>
  <div class="h-full">
    <div>
      <IconBuildingStore />
      <h1>Select store</h1>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useUserStore } from "@/store/user";
import { IconBuildingStore } from "@tabler/icons-vue";

const { getUser } = useUserStore();
getUser();
</script>
