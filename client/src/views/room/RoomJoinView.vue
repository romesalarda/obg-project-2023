<template>
<q-page class="q-pa-xs no-scroll" padding>
    <!-- header  -->
    <q-card style="width:65vh;padding:5vh" class="absolute-center bg-grey-3 shadow-15">
        <div class="text-h2 main-font text-center text-weight-medium q-pb-md">
            Access a room
        </div>
        <div class="text-h5 text-center q-pb-xl">Enter the details of the room bellow</div>
        <!-- domain name input -->
        <div class="q-gutter-md">
            <div class="fit row wrap justify-center items-start">
                <q-input filled v-model="domainName" label="Domain *" hint="domain" lazy-rules type="text" :error="error" :rules="[val => !!val || 'A domain name is required',]" style="width:60vh">
                    <template v-slot:prepend>
                        <q-icon name="domain" />
                    </template>
                </q-input>
            </div>
            <!-- room code input -->
            <div class="fit row wrap justify-center items-start">
                <q-input filled v-model="roomCode" label="Room code *" hint="roomcode" lazy-rules type="text" :error="error" :error-message="errorMessage" :rules="[
              val => !!val || 'A room code is required',
              val => val.length === 8 || 'A code is 8 characters long',]" style="width:60vh">
                    <template v-slot:prepend>
                        <q-icon name="home" />
                    </template>
                </q-input>
            </div>

            <!-- submit button to request access -->
            <q-btn class="bg-teal-4 text-white" push size="20px" @click="handleAccess" label="Join" icon-right="login" />

        </div>

    </q-card>
    <q-banner inline-actions class="text-white bg-red absolute-bottom" v-if="errorMessage.length!==0">
        <div class="absolute-center">
            {{errorMessage}}
        </div>
        <template v-slot:action>
            <q-btn flat color="white" label="Dissmis" @click="errorMessage=''" />
        </template>
    </q-banner>
</q-page>
</template>

<script lang="ts">
import {
    axiosInstance
} from '@/api/axios';
import {
    defineComponent
} from 'vue';

export default defineComponent({
    name: 'RoomJoinView',
    data() {
        // define variables
        return {
            roomCode: "",
            domainName: "",
            // errors
            error: false,
            errorMessage: "",

            // maximum length the room code needs to be
            roomCodeLength: 8
        }
    },
    methods: {
        handleAccess() {
            // verify that the room does exist to allow access to the next stage
            // this.error = false
            // this.errorMessage = ""
            this.errorMessage = ""
            if (this.roomCode.length === this.roomCodeLength && this.domainName.length != 0) {
                axiosInstance.get(`api-rooms/rooms/${this.roomCode}/room_available/?domain=${this.domainName}`).then(
                    response => {
                        // push to room verification screen if the room was found
                        if (response.status === 200) {
                            this.$router.push({
                                name: "room-verification",
                                params: {
                                    code: this.roomCode,
                                    domain: this.domainName,
                                }
                            })
                        } else {
                            // display default error that was raised by the server            
                            // this.errorMessage = "Room with given domain and room code not found"
                            this.errorMessage = response.data.detail
                            this.error = true
                        }
                    }
                ).catch(
                    error => {
                        console.log(error.response);
                        if (error.response.status == "404") {
                            this.errorMessage = "Room was not found. Please ensure the room code and domain were typed in correctly"
                            this.error = true

                        } else {
                            this.errorMessage = error.response.data.detail
                            this.error = true

                        }
                    }
                )
            } else {
                // validation
                this.error = true
                if (this.roomCode.length <= 0) {
                    this.errorMessage = "room code is required"
                } else if (this.roomCode.length !== this.roomCodeLength) {
                    this.errorMessage = "room code must be 8 characters"
                } else if (this.domainName.length <= 0) {
                    this.errorMessage = "domain name is required"
                }

            }
        }
    }
});
</script>
