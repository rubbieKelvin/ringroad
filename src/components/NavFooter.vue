<template>
  <div class="py-2 flex items-center justify-center">
    <p class="text-gray-700 text-sm">&copy; {{ now.getFullYear() }}</p>
  </div>
</template>

<script lang="ts" setup>
const now = new Date();
</script>
