<template>
  <div class="">
    <!-- header -->
    <div
      class="px-5 flex justify-between items-center h-24 border-b border-b-slate-300"
    >
      <!-- text -->
      <div>
        <h2 class="text-2xl font-medium">Inventory</h2>
        <p class="text-sm">34 items</p>
      </div>

      <!-- buttons -->
      <div class="flex gap-4">
        <button>+</button>

        <button>...</button>
      </div>
    </div>

    <!-- toolbar -->
    <div class="h-14 border-b border-b-slate-300 flex">
      <!-- search -->
      <div
        class="flex items-center gap-2 px-4 border-r border-r-slate-300 min-w-[30%]"
      >
        <IconSearch :size="24" />
        <input
          type="text"
          class="flex-grow h-full outline-none"
          placeholder="Search inventory"
        />
      </div>

      <!-- category select -->
      <DropDown
        class="w-60"
        v-model="category"
        :icon="IconCategory"
        title="Category"
        :values="['bag', 'cat', 'box']"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import DropDown from "@/components/DropDown.vue";
import { IconSearch, IconCategory } from "@tabler/icons-vue";
import { ref } from "vue";

const category = ref(null);
</script>

<style scoped lang="scss">
button {
  @apply bg-gray-200 rounded-md h-10 w-10 flex items-center justify-center;
}
</style>
