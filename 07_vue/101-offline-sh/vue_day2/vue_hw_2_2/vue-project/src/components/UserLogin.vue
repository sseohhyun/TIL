<template>
  <div>
    <h1>조건문 연습하기</h1>
    <button @click="isLogin =! isLogin">Login/Logout</button>
    <template v-if="isLogin">
      <ul>
        <li>유저네임 : {{ user.userName }}</li>
        <li>관리자여부 : {{ user.isAdmin }}</li>
        <li>비밀번호 : {{ user.passWord }}</li>
      </ul>
    </template>
 </div> 
</template>


<script setup>
import { ref } from 'vue'

// 로그인 버튼 클릭
const isLogin = ref(true)

// 주어진 user 정보
const user = {
  userName: "admin",
  isAdmin: true,
  passWord: "1q2w3e4r"
  }
</script>


<style scoped>
</style>