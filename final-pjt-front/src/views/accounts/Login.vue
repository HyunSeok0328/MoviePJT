<template>
  <div class="d-flex flex-column align-items-center mt-5">
      <form class="m-5">
        <div class="group">      
          <input type="text" required v-model="credentials.username">
          <span class="highlight"></span>
          <span class="bar"></span>
          <label>ID</label>
        </div>

        <div class="group">      
          <input 
            type="password" 
            required
            v-model="credentials.password"
            @keyup.enter="login"
          >
          <span class="highlight"></span>
          <span class="bar"></span>
          <label>Password</label>
        </div>
      </form>
      <b-button variant="outline-danger" @click="login">Login</b-button>
    </div>
</template>

// <script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
      username: null,
      password: null,
      passwordConfirmation: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then((res) => {
          console.log(res.data)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          alert('잘못된 ID 혹은 비밀번호입니다!')
          console.log(err)
        })
      
    }
  }
}
</script>

<style scoped>
  .group 			  { 
    position:relative; 
    margin-bottom:70px; 
  }
  input 				{
    font-size:18px;
    padding:10px 10px 10px 5px;
    display:block;
    width:300px;
    border:none;
    border-bottom:1px solid #757575;
    background: transparent;
    color: white;
  }
  input:focus 		{ outline:none; }

  /* LABEL ======================================= */
  label 				 {
    color:#999; 
    font-size:18px;
    font-weight:normal;
    position:absolute;
    pointer-events:none;
    left:5px;
    top:10px;
    transition:0.2s ease all; 
    -moz-transition:0.2s ease all; 
    -webkit-transition:0.2s ease all;
  }

  /* active state */
  input:focus ~ label, input:valid ~ label 		{
    top:-20px;
    font-size:14px;
    color:#f72307;
  }

  /* BOTTOM BARS ================================= */
  .bar 	{ position:relative; display:block; width:300px; }
  .bar:before, .bar:after 	{
    content:'';
    height:2px; 
    width:0;
    bottom:1px; 
    position:absolute;
    background:#CC0000; 
    transition:0.2s ease all; 
    -moz-transition:0.2s ease all; 
    -webkit-transition:0.2s ease all;
  }
  .bar:before {
    left:50%;
  }
  .bar:after {
    right:50%; 
  }

  /* active state */
  input:focus ~ .bar:before, input:focus ~ .bar:after {
    width:50%;
  }

  /* HIGHLIGHTER ================================== */
  .highlight {
    position:absolute;
    height:60%; 
    width:100px; 
    top:25%; 
    left:0;
    pointer-events:none;
    opacity:0.5;
  }

  /* active state */
  input:focus ~ .highlight {
    -webkit-animation:inputHighlighter 0.3s ease;
    -moz-animation:inputHighlighter 0.3s ease;
    animation:inputHighlighter 0.3s ease;
  }

  /* ANIMATIONS ================ */
  @-webkit-keyframes inputHighlighter {
    from { background:#CC0000; }
    to 	{ width:0; background:transparent; }
  }
  @-moz-keyframes inputHighlighter {
    from { background:#CC0000; }
    to 	{ width:0; background:transparent; }
  }
  @keyframes inputHighlighter {
    from { background:#CC0000; }
    to 	{ width:0; background:transparent; }
  }
</style>
