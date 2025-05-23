<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<!-- Note: Based on Material-UI text input styling. -->
<!-- See: https://mui.com/material-ui/react-text-field/ -->
<template>
  <div
    class="primary-text relative inline-flex w-full flex-col space-y-2 align-top"
  >
    <label
      class="z-1 absolute"
      :class="{
        'translate-x-4 text-sm text-distinct-text': shrinkLabel,
        'translate-y-[1.125rem] pl-[12px]': !shrinkLabel,
      }"
      :for="id"
    >
      {{ label }}
    </label>
    <div
      class="border-box relative inline-flex select-none items-center text-left text-distinct-text"
    >
      <input
        @focus="shrinkLabel = true"
        @blur="handleBlur"
        :id="id"
        class="box-content h-5 w-full bg-transparent py-3 pl-[12px] pr-[10px] text-primary-text outline-none"
        type="text"
        v-bind="$attrs"
      />
      <span v-if="$slots.icons" class="flex items-center gap-2 px-[10px]">
        <slot name="icons"></slot>
      </span>

      <!-- Using a fieldset allows the label to overlay the border. -->
      <fieldset
        aria-hidden="true"
        class="pointer-events-none absolute inset-0 -top-[5px] bottom-0 rounded border pl-[12px] pr-[10px]"
        :class="{
          'border-action-red dark:border-action-red': hasError,
          'border-interactive': !hasError,
        }"
        :data-testid="`${id}-border`"
      >
        <legend
          class="invisible h-3 text-sm"
          :class="{ 'max-w-[0.01px]': !shrinkLabel }"
          data-testid="hidden-legend"
        >
          <!-- This span overlays the border when expanded. -->
          <span class="visible px-1 opacity-0">
            {{ label }}
          </span>
        </legend>
      </fieldset>
    </div>
  </div>
</template>

<script setup lang="ts">
defineOptions({
  inheritAttrs: false,
});

export interface Props {
  id: string;
  label: string;
  hasError?: boolean;
}

withDefaults(defineProps<Props>(), {
  hasError: false,
});

const shrinkLabel = ref<boolean>(false);

const handleBlur = (event: FocusEvent) => {
  const target = event.target as HTMLInputElement | null;
  if (!target?.value) {
    shrinkLabel.value = false;
  }
};
</script>
