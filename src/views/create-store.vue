<template>
  <div class="flex flex-col items-center justify-center">
    <div class="p-4 rounded-md flex flex-col gap-3 min-w-[30em]">
      <div class="flex gap-2 items-center">
        <IconBuildingStore :size="32" />
        <h1 class="text-2xl flex-grow">Create store</h1>
      </div>
      <div class="input-field" v-for="i in ['name', 'description']" :key="i">
        <label :for="i">{{ i }}</label>
        <input :name="i" type="text" :placeholder="i" />
      </div>
      <button @click="goToStore" class="bg-gray-300 py-2 rounded">Go</button>
    </div>
  </div>
</template>

<style lang="scss">
.input-field {
  @apply flex flex-col;

  > input {
    @apply border border-gray-300 rounded-md h-8 px-2;
  }
}
</style>

<script lang="ts" setup>
import { IconBuildingStore } from "@tabler/icons-vue";
import { useRouter } from "vue-router";

const router = useRouter();
function goToStore() {
  router.push({ name: "dashboard-home", params: { id: "dummy-id" } });
}
</script>
