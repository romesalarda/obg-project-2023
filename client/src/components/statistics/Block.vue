<template>
<q-card :class="colours[index]" style="width:80vh;min-height:14vh">

    <div class="row">
        <div class="col bg-grey-3" style="min-height:14vh">
            <div class="text-h6 text-black q-pa-sm row">Block<div class="text-bold q-ml-sm">[{{index+1}}] </div>
                <q-chip icon="subject">{{ block.length }}</q-chip>
            </div>
        </div>
        <div class="col-10">
            <div class="row q-pa-sm">
                <div v-for="code in block" :key="code" style="padding:5px">
                    <Subject :code="code" />
                </div>
            </div>
        </div>
    </div>
</q-card>
</template>

<script lang="js">
import {
    defineComponent
} from 'vue';
import Subject from './Subject.vue';

export default defineComponent({
    name: 'OptionItem',
    props: ["block", "index"],
    components: {
        Subject
    },
    data() {
        return {
            colours: this.$store.state.colours
        }
    }

});
</script>
