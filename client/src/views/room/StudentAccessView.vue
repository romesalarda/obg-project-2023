<template>
<q-page class="q-pa-none no-scroll" padding>
    <q-card style="width:60vh" class="absolute-center bg-grey-3 shadow-15">

        <div class="q-gutter-md q-pa-lg full-width">
            <div class="row justify-center text-h3 main-font text-weight-medium">
                Student access
            </div>
            <div class="text-h5 text-center">Enter your school credentials</div>
            <!-- email input -->
            <div class="row justify-center items-start">
                <q-input filled v-model="email" label="email *" hint="email" lazy-rules type="text" :error="error" :rules="[val => !!val || 'field is required']" style="width:60vh">
                    <template v-slot:prepend>
                        <q-icon name="mail" />
                    </template>
                </q-input>
            </div>

            <!-- first name input -->
            <div class="row justify-center">

                <q-input filled v-model="firstName" label="first name *" hint="first name" lazy-rules type="text" :error="error" :rules="[val => !!val || 'field is required']" style="width:60vh">
                    <template v-slot:prepend>
                        <q-icon name="person" />
                    </template>
                </q-input>
            </div>
            <!-- last name input -->
            <div class="row justify-center">

                <q-input filled v-model="lastName" label="last name *" hint="last name" lazy-rules type="text" :error="error" :error-message="errorMessage" :rules="[val => !!val || 'field is required']" style="width:60vh">
                    <template v-slot:prepend>
                        <q-icon name="person" />
                    </template>
                </q-input>
                <q-btn class="bg-teal-4 text-white" push size="20px" @click="attemptEnter" label="Continue" icon-right="login" />
            </div>

        </div>

    </q-card>
    <BannerComponent v-if="serverError" :message="serverErrorMessage" @dismiss="dismissAllErrors" colour="red" />

</q-page>
</template>

<script lang="ts">
import {
    axiosInstance
} from '@/api/axios';
import BannerComponent from '@/components/misc/BannerComponent.vue';
import {
    defineComponent
} from 'vue';

export default defineComponent({
    name: 'StudentCrendentials',
    components: {
        BannerComponent
    },
    data() {
        return {
            email: "",
            firstName: "",
            lastName: "",
            // error handling
            errorMessage: "",
            error: false,

            serverError: false,
            serverErrorMessage: ""

        }
    },
    methods: {
        attemptEnter() {
            this.error = false
            this.errorMessage = ""
            // do some validation

            // NOTE THIS VALIDATION IS FOR TESTING AND SHOULD BE REWORKED FOR MORE 
            // ACCURATE ERROR MESSAGES

            if (this.email.length != 0 && this.firstName.length != 0 && this.lastName.length != 0) {
                axiosInstance.post(`api-rooms/rooms/join/`, {
                    // room details
                    code: this.$route.params.code,
                    domain: this.$route.params.domain,
                    // student details
                    first_name: this.firstName,
                    last_name: this.lastName,
                    email: this.email

                }).then(
                    response => {

                        if (response.status === 200) {
                            // joining was successful
                            const studentID = response.data.student_uuid
                            const params = this.$route.params
                            this.$router.push({
                                name: "student-choice",
                                params: {
                                    domain: params.domain,
                                    code: params.code,
                                    id: studentID
                                }
                            })
                        } else {
                            // raise error message from the server
                            this.serverError = true
                            
                            this.serverErrorMessage = response.data.detail
                        }
                    }
                ).catch(err=>{
                    this.serverError = true
                    this.serverErrorMessage = err.response.data.detail
                })

            } else {
                // handle the error
                this.error = true
                if (this.email.length <= 0) {
                    this.errorMessage = "an email is required"
                } else if (this.lastName.length <= 0) {
                    this.errorMessage = "a last name is required"
                } else if (this.firstName.length <= 0) {
                    this.errorMessage = "a first name is required"
                }
            }
        },
        dismissAllErrors() {
            this.error = false
            this.errorMessage = ""
            this.serverError = false
            this.serverErrorMessage = ""
        }
    }
});
</script>
