<template>
<div style="min-height:70vh">
    <q-card class="absolute-center bg-grey-3 no-margin full-width full-height" square>
        <div class="row">
            <div class="col-8">
                <q-card square style="height:90vh">
                    <div class="row">
                        <div v-for="(i, index) in blocks" :key="i[0]" class="col q-pa-sm bg-grey-3">
                            <div class="text-h5 q-ma-xs">Block {{index+1}}

                                <q-chip icon="subjects">{{blocks[index].length}}</q-chip>
                            </div>
                            <q-scroll-area style="height:65vh">
                                <draggable class="list-group" :list="blocks[index]" :id=index item-key="id" :group="{ name: 'people', pull: true, put: true }" :move="moveSubject" @start="startMove" @change="changeSubject" @end="finishedMove">
                                    <template #item="{element}">
                                        <div :id="element">
                                            <q-card :class="current == element[0] ? 'bg-red-6 q-pa-xs' : 'bg-grey-4 q-pa-xs'" @click="current=element[0]" square style="min-height:5vh">
                                                <div class="row">
                                                    <div class="col-2 main-font">
                                                        <div class="text-bold">{{element[0].slice(0, 2)}}</div>
                                                    </div>
                                                    <div class="col-7 text-body2 main-font">
                                                        {{this.$store.state.options[element[0]]}}
                                                    </div>
                                                    <div class="col">
                                                        <!-- <q-chip icon="account_circle">{{element[1]}}</q-chip> -->
                                                        <q-input v-model="element[1]" dense filled />
                                                    </div>
                                                </div>
                                            </q-card>
                                        </div>
                                    </template>
                                </draggable>
                            </q-scroll-area>
                        </div>
                        <div class="col q-ma-md">
                            <div class="text-h4 main-font text-weight-medium">Extra</div>
                            <div class="q-pa-md">
                                <div>Drag in extra subjects if required</div>
                            </div>
                            <q-scroll-area style="height:40vh">
                                <draggable class="list-group" item-key="id" :list="populatedOptions" :group="{ name: 'people', pull: 'clone', put: false }" :move="moveSubject" @start="startMove" @change="changeSubject" @end="addSubject">
                                    <template #item="{element}">
                                        <div :id="element">
                                            <q-card square :class="current == element[0] ? 'bg-blue-5 q-pa-xs text-white text-bold main-font' : 'bg-grey-3 q-pa-xs main-font'" @click="current=element[0]">
                                                {{element[0]}}, {{this.$store.state.options[element[0]]}}
                                            </q-card>
                                        </div>
                                    </template>
                                </draggable>
                            </q-scroll-area>
                            <div class="bg-grey-6 q-mt-md" style="height:13vh">
                                <div class="text-h6 text-white">
                                    <q-btn flat icon="delete" class="text-white" />
                                </div>
                                <draggable class="list-group" item-key="id" :list="[]" :group="{ name: 'trash', pull: false, put: true }" id="trash">
                                    <template #item="{element}">
                                        <div id="trash">
                                            <q-card class="bg-grey-6 q-pa-sm" square>
                                                {{element}}
                                            </q-card>
                                        </div>
                                    </template>
                                </draggable>
                                <div class="text-body1 text-white q-pa-sm main-font">
                                    Drag subjects above to delete them
                                </div>
                            </div>
                        </div>

                    </div>
                </q-card>
            </div>
            <div class="col-4">
                <q-card square style="height:80vh" class="bg-grey-3" flat>
                    <div class="text-h4 main-font text-weight-medium">Statistics</div>
                    <q-card-section>
                        <div class="row">
                            <div class="col-7">

                                <div class="row">
                                    <q-chip icon="schedule">Generation time : {{ this.$store.state.debug_data.generation_time }} seconds</q-chip>
                                </div>
                                <div class="row">
                                    <q-chip icon="subjects">Total subjects : {{ totalSubjects }}</q-chip>
                                </div>

                                <div class="row">
                                    <q-chip icon="subject">Students per subject total : {{ this.blockMeta.failed + this.blockMeta.counts}}</q-chip>
                                </div>
                            </div>
                            <div class="col">
                                <div class="row">
                                    <q-chip icon="account_circle">Success : {{ this.$store.state.success_percentage }} % </q-chip>
                                </div>
                                <div class="row">
                                    <q-chip icon="emoji_objects">Completed nodes : {{ this.$store.state.debug_data.completed_nodes }}</q-chip>

                                </div>
                                <div class="row">
                                    <q-chip icon="currency_pound">Total cost : {{ new Intl.NumberFormat('en-US', {style: 'currency',currency: 'GBP',}).format(this.$store.state.total_cost) }}</q-chip>

                                    
                                </div>

                            </div>
                        </div>

                    </q-card-section>
                    <q-separator />

                    <q-card-section class="bg-grey-4" style="height:33vh">
                        <div class="row">
                            <div class="col">
                                <div class="text-h4 main-font text-weight-medium">
                                    Operations
                                </div>
                                <div>
                                    Linear will evaluate each operation depedent on the results of the previous operation.
                                    <q-toggle v-model="linear" label="linear" />
                                </div>
                                <div class="row bg-grey-3 justify-center">
                                    <div class="col-1 q-pa-sm text-bold justify-center items-center bg-grey-5">
                                        ID
                                    </div>
                                    <div class="col-2 q-pa-sm text-bold justify-center items-center bg-grey-5">
                                        Type
                                    </div>
                                    <div class="col-5 q-pa-sm text-bold justify-center items-center">
                                        Details
                                    </div>
                                    <div class="col q-pa-sm text-bold justify-center items-center">

                                    </div>
                                </div>
                                <q-separator />
                                <q-scroll-area style="height:10vh">
                                    <div v-if="operations.length !== 0">
                                        <div v-for="(op, index) in operations" :key="index">
                                            <q-card class="bg-grey-3" square flat>
                                                <div class="row justify-center items-center">
                                                    <div class="col-1 justify-center items-center q-pa-sm">
                                                        {{op.id}}
                                                    </div>
                                                    <div class="col-2 justify-center items-center">
                                                        {{op.type}}
                                                    </div>
                                                    <div class="col-5 justify-center items-center">
                                                        <div v-if="op.type==='MOVE'">
                                                            <div class="text-body1 text-center">Moving '{{op.subject}}' Block [{{op.target+1}}] to [{{op.to+1}}]</div>

                                                        </div>
                                                        <div v-else-if="op.type==='ADD'">
                                                            <div class="text-body1 text-center">Adding '{{op.subject}}' to Block [{{op.block+1}}]</div>

                                                        </div>
                                                        <div v-else-if="op.type==='REMOVE'">
                                                            <div class="text-body1 text-center">Removing '{{op.subject}}' from Block [{{op.block+1}}]</div>

                                                        </div>

                                                    </div>
                                                    <div class="col justify-center items-center">
                                                        <q-btn-group>
                                                            <q-btn flat class="bg-red-6 text-white" size="sm" label="delete" @click="removeOperation(op)" />
                                                            <q-btn flat class="bg-blue-6 text-white" size="sm" label="undo" @click="undoOperation(op)" />

                                                        </q-btn-group>
                                                    </div>
                                                </div>
                                            </q-card>
                                        </div>
                                    </div>
                                    <div v-else>
                                        <q-card class="q-pa-sm bg-grey-3" square flat>
                                            <div class="text-body1">
                                                Changes to the option blocks will show up here
                                            </div>
                                        </q-card>
                                    </div>
                                </q-scroll-area>

                            </div>
                        </div>
                    </q-card-section>
                    <q-btn-group class="bg-grey-4 full-width row justify-center q-pa-sm">
                        <q-btn push class="bg-teal-4 text-white" size="md" label="evaluate blocks" @click="evaluate" />
                        <q-btn push class="bg-blue text-white" size="md" label="reset blocks" @click="reset" />
                        <q-btn push class="bg-blue text-white" size="md" label="remaining students" @click="remainingStudentsPopup = true" />
                    </q-btn-group>

                    <q-separator />
                    <q-btn-group class="row q-pa-lg">
                        <q-btn push class="bg-teal-4 text-white" size="md" label="pre statistics" icon="trending_up" @click="$emit('back')" />
                        <q-btn push class="bg-teal-3 text-white" size="md" label="save" icon="save_as" @click="savePopup = true" />
                        <q-btn push class="bg-teal-3 text-white" size="md" label="exit" color="red" @click="restart" icon="close" />

                    </q-btn-group>
                </q-card>
            </div>
        </div>
    </q-card>
    <q-dialog v-model="evaluationPopup">
        <q-card style="width:100vh;height:60vh">
            <q-card-section>
                <div class="text-h6 text-center">Results</div>

            </q-card-section>

            <q-card-section class="q-pt-none text-body1">
                <div class="row q-pa-sm bg-grey-3 justify-center items-center">
                    <div class="col-1 text-center main-font">
                        ID
                    </div>
                    <div class="col-2 text-center main-font">
                        Type
                    </div>
                    <div class="col-2 text-center main-font">
                        % Change
                    </div>
                    <div class="col-4 text-center main-font">
                        # student change
                    </div>
                    <div class="col text-center main-font">
                        Detail
                    </div>
                </div>
                <q-card v-for="result in evaluationResults" :key="result.id" square flat class="q-pa-sm bg-grey-4">
                    <div class="row ">
                        <div class="col-1 text-center main-font">
                            {{ result.id + 1 }}
                        </div>
                        <div class="col-2 text-center main-font">
                            {{ result.type }}
                        </div>
                        <div class="col-2 text-center main-font">
                            {{ result.info.success_change }}
                        </div>
                        <div class="col-4 text-center main-font">
                            {{ result.info.students_difference }}
                        </div>
                        <div class="col text-center main-font">
                            {{ result.detail }}
                        </div>
                    </div>
                </q-card>
                <q-card v-if="evaluationResults.length === 0" style="height:40vh" class="row justify-center items-center" square flat>
                    <div class="text-h4">No operations were commited</div>
                </q-card>

            </q-card-section>

        </q-card>
    </q-dialog>
    <q-dialog v-model="savePopup">
        <q-card>
            <q-card-section>
                <div class="text-h6 text-center main-font">Save these blocks so you can access them later!</div>
            </q-card-section>

            <q-card-section class="q-pt-none text-body1">
                <q-input label="title" v-model="title" :rules="[val=>val.length > 5 || 'title must be longer than 5 characters']" />
                <q-toggle v-model="useCurrentBlocks" label="use current blocks" />
            </q-card-section>

            <q-card-actions align="right">
                <q-btn label="RESTART" color="red" @click="restart" />
                <q-btn label="SAVE" color="primary" @click="saveBlocks" v-if="title.length > 5" />

            </q-card-actions>
        </q-card>
    </q-dialog>
    <q-dialog v-model="remainingStudentsPopup">
        <q-card>
            <q-card-section>
                <div class="text-h6 text-center main-font">Here are students we could not assign classes to</div>
                <div class="text-body2 text-center main-font">
                    This happens when there are not enough classes and we have placed the max number of students in a given class.
                    You will need to decide if more classes are needed or you can increase the number of students in a given class.
                
                </div>
            </q-card-section>

            <q-card-section class="q-pt-none text-body1">
                <div class="row q-pa-sm bg-grey-3 justify-center items-center">
                    <div class="col-2 text-center main-font">
                        Subject
                    </div>
                    <div class="col text-center main-font">
                        Number of students unassigned
                    </div>
                </div>
                <q-scroll-area style="height:30vh">

                <div v-for="subject in Object.entries(this.blockMeta.remaining) " :key="subject">
                    <q-card v-if="subject[1] > 0" flat class="q-pa-md bg-grey-4">
                        <div class="row q-pa-smjustify-center items-center">
                            <div class="col-2 text-center main-font">
                                {{subject[0]}}
                            </div>
                            <div class="col text-center main-font">
                                {{ subject[1] }} students
                            </div>
                        </div>
                    </q-card>
                </div>
                </q-scroll-area>
            </q-card-section>

            <q-card-actions align="right">
                <q-btn label="ok" v-close-popup flat/>

            </q-card-actions>
        </q-card>
    </q-dialog>
    <div class="absolute-bottom-right q-mb-lg q-mr-xl">

    </div>

    <BannerComponent colour="red" @dismiss="dismissError" v-if="errorMessage" :message="errorMessage" />
    <BannerComponent colour="green" @dismiss="successMessage=''" v-if="successMessage" :message="successMessage" />

</div>
</template>

<script lang="js">
import draggable from "vuedraggable";

import {
    defineComponent,
    ref
} from 'vue';
import {
    axiosInstance
} from "@/api/axios";
import BannerComponent from "../misc/BannerComponent.vue";

export default defineComponent({
    name: 'PreStatisticsView',
    emits: ["back", "next", "error", "dismissError"],
    components: {
        draggable,
        BannerComponent
    },
    data() {
        return {
            blocks: this.$store.state.generated_blocks.map(function (arr) {
                return arr.slice();
            }),
            current: "",
            operations: [],
            errorMessage: "",
            successMessage: "",
            blockMeta: this.$store.state.blocks_meta,
            linear: false,
            evaluationPopup: false,
            savePopup: false,
            remainingStudentsPopup: false,
            useCurrentBlocks: false,
            title: "",
            evaluationResults: []
        }
    },
    computed: {
        totalSubjects() {
            var count = 0
            this.blocks.forEach(item => {
                count = count + item.length
            })
            return count
        },
        populatedOptions() {
            const newObj = []
            for (const key of Object.keys(this.$store.state.options)) {
                newObj.push([key, 0])
            }
            return newObj
        }
    },
    methods: {
        moveSubject(event, _og) {
            // move subject

            let allow = true
            event.relatedContext.list.forEach(items=> {
                if (items[0] == event.draggedContext.element[0]) {
                    this.errorMessage = `'${event.draggedContext.element}' already exists in this block`
                    allow = false
                }
            })
            return allow
        },
        changeSubject(event) {
            // NOTE: used for debug only
            // console.log(event);
        },
        startMove(arg) {
            this.$emit("dismissError")
            this.current = arg.item.id
        },
        finishedMove(event) {
            // called whenever a subject is moved. We need to track if it was moved to the trash or to a different
            // block.
            if (event.to !== event.from) {
                if (event.to.id === 'trash') {
                    this.operations.push({
                        id: this.operations.length + 1,
                        type: "REMOVE",
                        block: Number(event.from.id),
                        subject: event.clone.id.split(",")[0],
                        students: event.clone.id.split(",")[1],
                        detail: `Removing '${event.clone.id}' from Block ${Number(event.from.id)+1}`
                    })
                } else {

                    this.operations.push({
                        id: this.operations.length + 1,
                        type: "MOVE",
                        target: Number(event.from.id),
                        subject: event.clone.id.split(",")[0],
                        students: event.clone.id.split(",")[1],
                        to: Number(event.to.id),
                        detail: `Moving '${event.clone.id}' Block ${Number(event.from.id)+1} to ${Number(event.to.id)+1}`
                    })
                }
            }
        },
        addSubject(event) {
            // ADD subject operation
            if (event.to !== event.from) {
                this.operations.push({
                    id: this.operations.length + 1,
                    type: "ADD",
                    subject: event.clone.id.split(",")[0],
                    students: event.clone.id.split(",")[1],
                    block: Number(event.to.id),
                    detail: `Adding '${event.item.id}' to Block ${Number(event.to.id)+1}`
                })
            }
        },
        removeOperation(operation) {
            // remove a given operation
            this.operations = this.operations.filter(op => op.id !== operation.id)
        },
        undoOperation(operation) {
            // attempts to undo a given operation. It may not be successful so it will
            // set an error message when needed
            let type = operation.type
            let success = false
            // undo add operation by doing a remove operation
            if (type === "ADD") {
                let newBlocks = []
                let found = false
                this.blocks.forEach((block, index) => {
                    if (index == operation.block) {
                        newBlocks.push(block.filter(subject => {
                            if (subject[0] === operation.subject && found === false) {
                                found = true
                            }
                            return subject[0] !== operation.subject
                        }))
                    } else {
                        newBlocks.push(block)
                    }
                })
                if (found === false) {
                    this.errorMessage = "Could not undo [ADD] operation as the subject no longer exists in the block"
                } else {

                    this.blocks = newBlocks
                    success = true
                }
                // undo a REMOVE operation by doing an add operation
            } else if (type === "REMOVE") {
                let found = false
                this.blocks[operation.block].forEach(
                    subject => {
                        if (subject === operation.subject) {
                            found = true
                        }
                    }
                )
                if (found === true) {
                    this.errorMessage = "Could not undo [REMOVE] operation as the subject already exists within this block"
                } else {
                    this.blocks[operation.block].push([operation.subject, operation.students])
                    success = true
                }
            }
            // undo MOVE operation by reversing the move
            else if (type === "MOVE") {
                if (this.subjectInBlock(operation.target, operation.subject)) {
                    this.errorMessage = `Cannot undo [MOVE] operation as '${operation.subject}' already exists in the original block [${operation.target+1}]`
                } else {
                    let found = false
                    let newBlocks = []
                    this.blocks.forEach((block, index) => {
                        // pop from the current block
                        if (index == operation.to) {
                            newBlocks.push(block.filter(subject => {
                                if (subject[0] === operation.subject && found === false) {
                                    found = true
                                }
                                return subject[0] !== operation.subject
                            }))
                            // add to the original block
                        } else if (index == operation.target) {
                            block.push([operation.subject, operation.students])
                            newBlocks.push(block)
                        } else {
                            newBlocks.push(block)
                        }
                    })
                    if (found === false) {
                        this.errorMessage = "Could not undo [MOVE] operation as the subject no longer exists in the block"
                    } else {
                        this.blocks = newBlocks
                        success = true
                    }
                }
            }

            if (success === true) {
                this.removeOperation(operation)
            }

        },
        dismissError() {
            this.errorMessage = ""
        },
        reset() {
            // resets everything as if we just finished generation
            this.blocks = this.$store.state.generated_blocks.map(function (arr) {
                    return arr.slice();
                }),
                this.current = ""
            this.operations = []
            this.dismissError()
        },
        evaluate() {
            // send request to evaluate operations the user has comitted
            this.popup = false
            axiosInstance.post("api-generate/generator/evaluate/", {
                initial: this.$store.state.generated_blocks,
                all_students: this.$store.state.all_students,
                new: this.blocks,
                operations: this.operations,
                linear: this.linear,
                meta: this.blockMeta,
                options: this.$store.state.options,
            }).then(response => {
                this.evaluationPopup = true
                this.evaluationResults = response.data.report
                this.blockMeta = response.data.meta
            }).catch(
                error => {
                    this.errorMessage = error.response.data.detail
                }
            )
        },
        subjectInBlock(block, target) {
            // returns bool whether or not a subject exists within a block
            let found = false
            this.blocks[block].forEach(
                subject => {
                    console.log(subject);
                    if (subject == target) {
                        found = true
                    }
                })
            return found
        },
        saveBlocks() {
            // saves blocks
            var blocks = []
            if (this.useCurrentBlocks === false) {
                blocks = this.$store.state.generated_blocks
            } else {
                blocks = this.blocks
            }
            axiosInstance.post(`api-generate/option-blocks/`, {
                blocks: blocks,
                code: this.$route.params.room_id,
                title: this.title,
                success: this.$store.state.success_percentage,
                generation_time: this.$store.state.debug_data.generation_time,
                completed_nodes: this.$store.state.debug_data.completed_nodes,
                generated_nodes: this.$store.state.debug_data.generated_nodes

            }).then(response => {
                this.successMessage = "saved successfully"
            }).catch(error => {
                this.errorMessage = error.response.data.detail
            })
        },
        restart() {
            this.$router.push({
                "name": "room-edit",
                params: {
                    user_id: this.$route.params.user_id,
                    room_id: this.$route.params.room_id,
                }
            })
        }
    },

});
</script>
