<template>
  <div class="min-w-[150px] relative">
    <div class="flex px-5 items-center gap-2 h-full" @click="open = !open">
      <!-- icon -->
      <component v-if="icon" :is="icon" :size="24" />
      <!-- text -->
      <div class="flex-grow select-none">
        <p class="text-sm">{{ title }}</p>
        <slot name="display" :value="selection">
          <p>{{ selection ?? "No value" }}</p>
        </slot>
      </div>
      <!-- icon -->
      <div>
        <IconChevronUp v-if="open" :size="18" />
        <IconChevronDown v-else :size="18" />
      </div>
    </div>

    <div v-if="open" class="absolute w-full">
      <ul>
        <li v-for="item in values">
          <slot :value="item">
            <div class="px-5 py-2">
              {{ item }}
            </div>
          </slot>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { v4 as uuid4 } from "uuid";
import { IconChevronUp } from "@tabler/icons-vue";
import { IconChevronDown } from "@tabler/icons-vue";
import {
  FunctionalComponent,
  Ref,
  WritableComputedRef,
  computed,
  ref,
} from "vue";
import { usePopupStore } from "@/store/popup";

defineProps<{
  icon?: FunctionalComponent;
  title: string;
  values: Array<number | string>;
}>();

const id = uuid4();
const popupstore = usePopupStore();

const open: WritableComputedRef<boolean> = computed({
  set(v: boolean) {
    if (v) popupstore.setOpened(id);
    else popupstore.setOpened(null);
  },
  get(): boolean {
    return popupstore.currentlyOpened === id;
  },
});
const selection: Ref<string | number | null> = ref(null);
</script>
