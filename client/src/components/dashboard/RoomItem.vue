<template>
    <div class="row justify-center items-center">
        <q-card style="width:55vh;margin:1vh" class="bg-teal-3 glossy">
        <q-card-section>
            <div class="text-h5 text-white">{{room.domain}}/{{room.code}}</div>
        </q-card-section>
        <q-card-actions>
            <q-btn class="bg-blue-grey text-white" @click="$emit('onDelete', room)" icon="highlight_off" label="delete room"/>
            <q-btn class="bg-grey text-white" @click="$emit('onEdit', room)" icon="edit" label="edit room"/>

        </q-card-actions>
        </q-card>
    </div>
</template>
<script lang="js">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'AvailableOption',  
    props: ["room"],
    emits: ["onDelete", "onEdit"]
});

</script>