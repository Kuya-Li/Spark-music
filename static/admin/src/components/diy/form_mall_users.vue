<template>
	<div>
			<el-form-item v-if="$check_register_field('add','user_number','/mall_users/view')" label="用户编号" prop="user_number">
				<el-input id="user_number" v-model="form['user_number']" placeholder="请输入用户编号"></el-input>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','full_name','/mall_users/view')" label="姓名" prop="full_name">
				<el-input id="full_name" v-model="form['full_name']" placeholder="请输入姓名"></el-input>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','age','/mall_users/view')" label="年龄" prop="age">
				<el-input id="age" v-model="form['age']" placeholder="请输入年龄"></el-input>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','gender','/mall_users/view')" label="性别" prop="gender">
				<el-select id="gender" v-model="form['gender']">
			<el-option v-for="o in list_gender" :key="o" :label="o" :value="o">
			</el-option>
		</el-select>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','category','/mall_users/view')" label="类别" prop="category">
				<el-select id="category" v-model="form['category']">
			<el-option v-for="o in list_category" :key="o.category" :label="o.category"
				:value="o.category">
			</el-option>
		</el-select>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','resume','/mall_users/view')" label="简历" prop="resume">
				<el-upload id="resume" class="avatar-uploader" drag
			accept="image/gif, image/jpeg, image/png, image/jpg" action="" :http-request="uploadimg"
			:show-file-list="false" >
			<img v-if="form['resume']" :src="$fullUrl(form['resume'])" class="avatar">
			<i v-else class="el-icon-plus avatar-uploader-icon"></i>
		</el-upload>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','remarks','/mall_users/view')" label="备注" prop="remarks">
				<el-input type="textarea" id="remarks" v-model="form['remarks']" placeholder="请输入备注"></el-input>
				</el-form-item>
	
	</div>
</template>

<script>
	import mixin from "@/mixins/component.js";

	export default {
		mixins: [mixin],
		props:{

			form:{
				type: Object,
				default: function(){
					return {
							"user_number":  '' ,
								"full_name":  '' ,
								"age":  '' ,
								"gender":  '' ,
								"category":  '' ,
								"resume":  '' ,
								"remarks":  '' ,
						}
				}
			},

		},
		data() {
			return {
				field: "mall_users_id",
				url_add: "~/api/mall_users/add?",
				url_set: "~/api/mall_users/set?",
				url_upload: "~/api/mall_users/upload?",

										list_gender: ['男','女'],
								list_category: [""],
							rules: {
					"user_number": [    {required: true,message: '用户编号不能为空'},  ],
					"full_name": [    {required: true,message: '姓名不能为空'},  ],
					"age": [    {required: true,message: '年龄不能为空'},  ],
					"gender": [    {required: true,message: '性别不能为空'},  ],
					"category": [    {required: true,message: '类别不能为空'},  ],
					"resume": [    {required: true,message: '简历不能为空'},  ],
					"remarks": [    {required: true,message: '备注不能为空'},  ],
				}

			}
		},
		methods: {

	
	
	

	
	
	

	
	
	

	
	
	

	
	
				/**
			 * 获取类别列表
			 */
			async get_list_category() {
				var list = await this.$get("~/api/classification_information/get_list?");
				this.list_category = list.result.list;
			},
					

				/**
			 * 上传简历
			 * @param {Object} param 图片参数
			 */
			uploadimg(param) {
				this.uploadFile(param.file, "resume");
			},
	
	
	

	
	
	

		},
		created() {
								this.get_list_category();
					}
	}
</script>
