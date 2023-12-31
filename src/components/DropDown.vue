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

    <div
      v-if="open"
      class="absolute w-full z-10 border shadow-lg border-slate-100"
    >
      <ul>
        <li v-for="item in values" @click="() => select(item)">
          <slot :value="item">
            <div class="px-5 py-2.5 bg-white hover:bg-gray-100">
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
import { FunctionalComponent, WritableComputedRef, computed } from "vue";
import { usePopupStore } from "@/store/popup";

const props = defineProps<{
  icon?: FunctionalComponent;
  title: string;
  modelValue: string | number | null;
  values: Array<number | string>;
}>();

const emit = defineEmits(["selected", "update:modelValue"]);

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

const selection: WritableComputedRef<string | number | null> = computed({
  get() {
    return props.modelValue;
  },
  set(v) {
    emit("update:modelValue", v);
  },
});

function select(item: number | string | null) {
  selection.value = item;
  open.value = false;
  emit("selected", item);
}
</script>
