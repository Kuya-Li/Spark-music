<template>
  <div class="vw1">
	<h3 class="tittle">智能机器人</h3>
	<button @click="doClose" class="Colse">关闭</button>
    <iframe src="https://chatgpt.qdymys.cn/#/chat" width="100%" height="500px"></iframe>

   

    </div>
  </div>
</template>

<script>

import axios from 'axios'
export default {
	name:'right',
	props:{
		dialog_visible:Boolean
	},
    data() {
        return {
           
			visible: this.dialog_visible
        }
    },
	watch:{
		visible(val){
			this.dialog_visible = val;
		}
	},
    methods:{
        
		doClose(){
			this.$emit('dialogVisibleEvent',false)
		}
    }
}
</script>

<style lang="scss" >
	.title-s{
		display: flex;
		margin-right: 81px;

	}
	.tiles-text{
		line-height: 2rem;
    	background-color: #c8c8c8;
    	position: relative;
    	left: 23px;
    	border-radius: 9px;
    	font-size: 13px;
    	padding-left: 8px;
    	padding-right: 8px;
		color: #000000;
	}

	.tiles-text::before{
		content: '';
		position: absolute;
		border: 11px solid #000;
		border-top-color: transparent;
		border-bottom-color: transparent;
		border-left-color: transparent;
		border-right-color: #c8c8c8;
		left: -27px;
		top: 6px;

	}
	.tishi{
		position: fixed;
		bottom: 60px;
		width: 85px;
		background-color: #3a4750;
		color: #f1f1f1;
		padding: 5px;
		border-radius: 5px;
		right: 31px;
	}

	.tishi::before{
		left: 3px;
		content: '';
		position: absolute;
		top: 31px;
		border: 8px solid #000;
		border-top-color: #3a4750;
		border-bottom-color: transparent;
		border-left-color: transparent;
		border-right-color: transparent;
	}

 .ip1{
	   caret-color: #4e6ef2;
	   /* position: relative; */
	   z-index: 17;
	   box-sizing: border-box;
	   display: block;
	   padding: 10px 20px;
	   margin: 0 !important;
	   margin-left: 0 !important;
	   height: 48px;
	   line-height: 20px;
	   width: inherit;
	   border-right: 1px solid #c8c8c8;
	   font-size: 18px;
	   color: #1f1f1f;
	   transition: .3s;
	   font-family: PingFangSC-Regular,Tahoma,Helvetica,"Microsoft Yahei","微软雅黑",Arial,STHeiti;
	   border-radius: 0px;

    }
    .bt1{
		height: 40px;
    	line-height: 39px;
    	background: #4c3b3b00;
    	border-radius: 10px;
    	box-shadow: 1 6px 1px 2px #015249;
    	font-size: 16px;
    	font-weight: 800;
    	border: 0;
    	color: #f3f6f8;
    	cursor: pointer;
		width: inherit;
    }
    .vw1{
	    width: 350px;
    height: 530px;
    flex: 4;
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;
    margin-top: 50px;
    position: relative;
    background-color: #ffffff;
    margin: 0 auto;
  
    border: 1px solid;
    border-radius: 5px;
	}
    .vw2{
	margin-bottom: 0px;
    width: 350px;
    background-color: #3a4750;
    display: flex;
    align-items: center;
    position: fixed;
    bottom: 151px;
    /* left: 5px; */
    margin-left: 7px;
    z-index: 9;
    }
    .vw3{
        margin-top:7px;
		display: flex;
    }
	.vw3 text{
		background: #332323;
		color: #f1f1f1;
		border-radius: 6px;
		line-height: 34px;
	}

	.vw4{
		display: flex;
		position: relative;
		width: 100%;
		margin-top: 13px;
	}
	.vw4-l{
		flex-direction: row-reverse;
	}

	.vw4-r{
		flex-direction: row;
	}
	.lf{
		display: flex;
		flex-direction: row;
	}
	.vw4-l{
		flex-direction: column;
	}



	.centers-ft{
		    width: 265px;
			position: relative;
			right: 18px;

			border-radius: 10px;
			display: flex;
			flex-direction: inherit;
	}

	.centers{

		   line-height: 2.0rem;
		   border-radius: 10px;
		   /* border-top-left-radius: 0; */
		   /* border-bottom-left-radius: 2px; */
		   margin-right: 6px;
		   font-size: 13px;
		   color: #fff;
		   overflow: hidden;
		   background-color: #3a4750;
		   padding-left: 8px;
		   padding-right: 8px;
	}
	.centers-ft::before{
		    content: '';
		    position: absolute;
		    top: 4px;
		    right: -22px;
		    height: 0px;
		    width: 0px;
		    border: 11px solid #000;
		    border-top-color: transparent;
		    border-bottom-color: transparent;
		    border-left-color: #3a4750;
		    border-right-color: transparent;
	}

	.nones-imgse{
		border-radius: 5px !important;
		margin-right: 5px;
		position: relative;
	}
	.nones-imgse::before{
		content: '';
		position: absolute;
		width: 35px;
		height: 35px;
		background-image: url("../../../public/you.jpg");
		background-size: 100% cover;
	}

	.tittle{
		background-color: #1208087d;
    width: 100%;
    text-align: center;
    height: 50px;
    display: block;
    margin: 0;
    line-height: 50px;
    color: #ffffff;
	margin-bottom: 0px;
	}


	


		/* // .centers-ft:nth-last-of-type{
		// 	margin-bottom: 50px;
		// } */

		

	
	.nones-l{
		display: flex;
		flex-direction: row-reverse;
	}

	.noes{
		width: 35px;
    	height: 35px;
    	background-color: #aebecb;
    	border-radius: 5px;
    	margin-left: 5px;

	}

	html::-webkit-scrollbar-thumb:window-inactive {
    background: rgb(160, 87, 221);
}

.Colse{
	position: absolute;
    right: 0px;
    background-color: #22222285;
    border-radius: 5px;
    border: 1px;
    color: #f1f1f1;
	width: 58px !important;
}


</style>
