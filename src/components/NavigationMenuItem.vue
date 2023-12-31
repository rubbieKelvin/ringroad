<template>
  <RouterLink
    :to="link"
    class="flex gap-2 items-center px-2 py-2.5 hover:bg-gray-100 select-none rounded-md"
  >
    <!-- icon -->
    <component :is="icon" :size="24" />
    <!-- text -->
    <p class="text-lg flex-grow">{{ text }}</p>
    <!-- badge -->
    <div
      v-if="badge"
      class="px-1.5 py-0.5 min-w-[1.8em] text-sm rounded-full bg-gray-300 flex items-center justify-center"
    >
      <p>{{ badge }}</p>
    </div>
  </RouterLink>
</template>

<script setup lang="ts">
import { FunctionalComponent } from "vue";

defineProps<{
  icon: FunctionalComponent;
  text: string;
  badge?: string;
  link: string | { name: string; params?: any };
}>();
</script>
