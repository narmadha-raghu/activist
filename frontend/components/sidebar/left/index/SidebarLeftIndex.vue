<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<template>
  <div
    class="elem-shadow-sm mx-1 rounded-md bg-layer-2 pb-1 pt-2 text-primary-text transition-all duration-500"
  >
    <div class="flex flex-col items-center">
      <div
        v-if="sidebarTypeToDisplay === SidebarType.ORGANIZATION_PAGE"
        class="relative"
        :class="{
          'h-32 w-32':
            sidebar.collapsed == false || sidebar.collapsedSwitch == false,
          'h-10 w-10':
            sidebar.collapsed == true && sidebar.collapsedSwitch == true,
        }"
      >
        <button
          v-if="sidebar.collapsed == false || sidebar.collapsedSwitch == false"
          @click="openModal()"
          class="focus-brand absolute bottom-1 right-1 z-10 flex rounded-md border border-black/80 bg-white/80 p-[0.125em] text-black/80 dark:border-white/80 dark:bg-black/80 dark:text-white/80"
        >
          <Icon :name="IconMap.PLUS" size="1em" />
        </button>
        <!-- Attn: Disabled -->
        <!-- <ModalUploadImages @closeModal="handleCloseModal" :uploadLimit="1" /> -->
        <ImageOrganization
          class="elem-shadow-sm"
          :imgUrl="logoUrl"
          :alt="
            $t('i18n._global.entity_logo', {
              entity_name: name,
            })
          "
        />
      </div>
      <div
        v-else-if="sidebarTypeToDisplay === SidebarType.EVENT_PAGE"
        class="relative"
        :class="{
          'h-32 w-32':
            sidebar.collapsed == false || sidebar.collapsedSwitch == false,
          'h-10 w-10':
            sidebar.collapsed == true && sidebar.collapsedSwitch == true,
        }"
      >
        <button
          v-if="sidebar.collapsed == false || sidebar.collapsedSwitch == false"
          @click="openModal()"
          class="focus-brand absolute bottom-1 right-1 z-10 flex rounded-md border border-black/80 bg-white/80 p-[0.125em] text-black/80 dark:border-white/80 dark:bg-black/80 dark:text-white/80"
        >
          <Icon :name="IconMap.PLUS" size="1em" />
        </button>
        <ModalUploadImages @closeModal="handleCloseModal" :uploadLimit="1" />
        <ImageEvent
          class="elem-shadow-sm"
          eventType="action"
          :alt="
            $t('i18n._global.entity_logo', {
              entity_name: name,
            })
          "
        />
      </div>
      <ul
        id="submenu"
        class="mb-1 flex w-full flex-col px-1"
        :class="{
          'mt-4':
            sidebar.collapsed == false || sidebar.collapsedSwitch == false,
          'mt-2': sidebar.collapsed == true && sidebar.collapsedSwitch == true,
        }"
      >
        <li
          v-for="menuEntry in sidebarTypeToDisplay ===
          SidebarType.ORGANIZATION_PAGE
            ? menuEntriesState.organizationEntry.value
            : menuEntriesState.eventEntry.value"
        >
          <SidebarLeftSelector
            :id="
              (sidebarType === SidebarType.ORGANIZATION_PAGE
                ? 'org-'
                : 'event-') + menuEntry.label.split('.').pop()
            "
            :label="menuEntry.label"
            :routeUrl="menuEntry.routeUrl"
            :iconUrl="menuEntry.iconUrl"
            :selected="menuEntry.selected"
          />
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { IconMap } from "~/types/icon-map";
import { SidebarType } from "~/types/sidebar-type";

const props = defineProps<{
  name: string;
  sidebarType: SidebarType.ORGANIZATION_PAGE | SidebarType.EVENT_PAGE;
  logoUrl?: string;
}>();

const sidebarTypeToDisplay = computed(() => props.sidebarType);

const sidebar = useSidebar();
const menuEntriesState = useMenuEntriesState();
const modals = useModals();
const modalName = "ModalUploadImages";
const modalIsOpen = ref(false);

function openModal() {
  modals.openModal(modalName);
  modalIsOpen.value = modals.modals[modalName].isOpen;
}

const handleCloseModal = () => {
  modals.closeModal(modalName);
  modalIsOpen.value = modals.modals[modalName].isOpen;
};
</script>
