<template>
<q-page class="q-pa-xl" padding>
    <q-card style="width:60vh;padding:5vh" class="absolute-center bg-grey-3 shadow-15">

        <div class="text-h2 text-center main-font text-weight-bold">
            Teacher login
        </div>
        <div class="text-h5 text-center q-pa-lg main-font">Enter your credentials bellow</div>
        <q-form @submit="handleLogin()" @reset="handleReset()" class="q-gutter-md">
            <q-input filled v-model="email" label="Your email *" hint="email" lazy-rules type="email" :error="error" :rules="[
                                val => !!val || 'An email is required']"
                                :error-message="errMsg"
                                >
                <template v-slot:prepend>
                    <q-icon name="mail" />
                </template>
            </q-input>

            <q-input filled v-model="password" label="Your password *" hint="password" lazy-rules type="password" autocomplete="on"  :error="error" :rules="[
                                val => !!val || 'A password is required']"
                                                                :error-message="errMsg"
>
                <template v-slot:prepend>
                    <q-icon name="password" />
                </template>
            </q-input>
            <div class="q-gutter-md">
                <q-btn class="bg-teal-4 text-white" push size="20px" @click="handleLogin" icon-right="login">
                    Login
                </q-btn>
                <q-btn class="bg-red-13 text-white" push size="20px" @click="handleReset" icon-right="restart_alt">
                    Reset
                </q-btn>
            </div>
        </q-form>
    </q-card>
</q-page>
</template>

<script lang="ts">
import {
    defineComponent
} from 'vue';
import {
    login,
    logout
} from '@/api/auth'
import jwt_decode from 'jwt-decode'
import {
    DecodedTokenObject
} from '@/api/interfaces'
export default defineComponent({
    name: "LoginView",
    data() {
        return {
            password: "",
            email: "",
            error: false,
            errMsg: ""
        }
    },
    methods: {
        handleLogin() {
            if (this.email.length > 0 && this.password.length > 0) {
                login({
                    'email': this.email,
                    'password': this.password
                }).then(
                    accessToken => {
                        
                        const decoded: DecodedTokenObject = jwt_decode(accessToken)

                        this.$router.push({
                            name: "user-dashboard",
                            params: {
                                user_id: decoded.user_id
                            }
                        
                        })

                    }
                ).catch(err => {
                    this.error = true                    
                    this.errMsg="Password or email was invalid"
                })
            }
            else {
                this.error = true                    
                this.errMsg="Password or email was invalid"
            }

        },
        handleReset() {
            this.password = ""
            this.email = ""
            this.error = false
            this.errMsg = ""
        }
    }
})
</script>
