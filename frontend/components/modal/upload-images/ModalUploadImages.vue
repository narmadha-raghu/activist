<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<template>
  <ModalBase :modalName="modalName">
    <div>
      <DialogTitle>
        <p v-if="uploadLimit > 1" class="responsive-h2 font-bold">
          {{ $t("i18n.components.modal_upload_images.upload_images") }}
        </p>
        <p v-else class="responsive-h2 font-bold">
          {{ $t("i18n.components.modal_upload_images.upload_an_image") }}
        </p>
      </DialogTitle>
      <div class="mt-4">
        <ModalUploadImagesFileDropZone
          v-if="files.length != uploadLimit"
          @files-dropped="handleFiles"
          v-slot="{ isDropZoneActive }"
        >
          <span v-if="isDropZoneActive && uploadLimit > 1">{{
            $t("i18n.components.modal_upload_images.drop_images")
          }}</span>
          <span v-else-if="isDropZoneActive && uploadLimit == 1">{{
            $t("i18n.components.modal_upload_images.drop_image")
          }}</span>
          <span v-else-if="!isDropZoneActive && uploadLimit > 1">{{
            $t("i18n.components.modal_upload_images.drag_images")
          }}</span>
          <span v-else-if="!isDropZoneActive && uploadLimit == 1">{{
            $t("i18n.components.modal_upload_images.drag_image")
          }}</span>
        </ModalUploadImagesFileDropZone>
        <p class="py-2">
          {{ $t("i18n.components.modal_upload_images.number_of_files") }}:
          {{ files.length }}
        </p>
        <p
          v-if="uploadLimit == 1 && files.length == uploadLimit"
          class="text-action-red"
        >
          {{ $t("i18n.components.modal_upload_images.picture_limit_1") }}
        </p>
        <p
          v-if="uploadLimit != 1 && files.length >= uploadLimit"
          class="text-action-red"
        >
          {{
            $t("i18n.components.modal_upload_images.picture_limit_multiple", {
              limit: uploadLimit,
            })
          }}
        </p>
        <div>
          <draggable
            v-model="files"
            tag="div"
            class="flex flex-row"
            animation="300"
            ghost-class="opacity-0"
          >
            <template #item="{ element: file }">
              <span class="pb-4">
                <button @click="removeFile(file)" class="text-action-red">
                  <Icon :name="IconMap.X_SM" size="1.5em" />
                </button>
                <img
                  :key="file.name"
                  :src="file.url"
                  class="h-20 w-20 object-contain"
                  :alt="
                    $t('i18n.components.modal_upload_images.upload_image') +
                    ' ' +
                    file.name
                  "
                />
              </span>
            </template>
          </draggable>
          <BtnAction
            v-if="files.length > 0"
            @click="handleUpload"
            :cta="true"
            :label="$t('i18n.components.modal_upload_images.upload')"
            fontSize="sm"
            :leftIcon="IconMap.ARROW_UP"
            iconSize="1.25em"
            :ariaLabel="'i18n.components._global.upvote_application_aria_label'"
            :disabled="files.length >= uploadLimit"
          />
        </div>
      </div>
    </div>
  </ModalBase>
</template>

<script setup lang="ts">
import { DialogTitle } from "@headlessui/vue";
import draggable from "vuedraggable";

import { IconMap } from "~/types/icon-map";

const { files, handleFiles, removeFile, uploadFiles } = useOrganizationImages();

export interface Props {
  uploadLimit?: number;
  organizationId?: string;
}

const props = withDefaults(defineProps<Props>(), {
  uploadLimit: 10,
  organizationId: undefined,
});

const modalName = "ModalUploadImages";
const uploadError = ref(false);

const emit = defineEmits(["upload-complete", "upload-error"]);

const handleUpload = async () => {
  try {
    await uploadFiles(props.organizationId);
    const modals = useModals();
    modals.closeModal(modalName);
    emit("upload-complete");
    uploadError.value = false;
  } catch (error) {
    console.error("Error uploading images:", error);
    emit("upload-error");
  }
};
</script>
