<template>
	<div>
			<b-form-group v-if="$check_register_field('add','user_number','/mall_users/view')" id="input-group-${idx}" label="用户编号" label-for="input-${idx}">
			<b-form-input id="input-${idx}" v-model="form['user_number']" type="text" placeholder="用户编号" trim></b-form-input>
		</b-form-group>
				<b-form-group v-if="$check_register_field('add','full_name','/mall_users/view')" id="input-group-${idx}" label="姓名" label-for="input-${idx}">
			<b-form-input id="input-${idx}" v-model="form['full_name']" type="text" placeholder="姓名" trim></b-form-input>
		</b-form-group>
				<b-form-group v-if="$check_register_field('add','age','/mall_users/view')" id="input-group-${idx}" label="年龄" label-for="input-${idx}">
			<b-form-input id="input-${idx}" v-model="form['age']" type="text" placeholder="年龄" trim></b-form-input>
		</b-form-group>
				<b-form-group v-if="$check_register_field('add','gender','/mall_users/view')" id="input-group-${idx}" label="性别" label-for="input-${idx}">
			<b-form-select id="input-${idx}" v-model="form['gender']" :options="getDropList(list_gender)"></b-form-select>
		</b-form-group>
				<b-form-group v-if="$check_register_field('add','category','/mall_users/view')" id="input-group-${idx}" label="类别" label-for="input-${idx}">
			<b-form-select id="input-${idx}" v-model="form['category']" :options="list_category"></b-form-select>
		</b-form-group>
				<div v-if="$check_register_field('add','resume','/mall_users/view')">
			<div>简历</div>
			<div>
				<input type="file" @change="uploadFile($event.target.files,'resume')" />
				<img v-if="form['resume']" style="width: 50px;height: 50px;" :src="$fullUrl(form['resume'])" />
			</div>
		</div>
				<b-form-group v-if="$check_register_field('add','remarks','/mall_users/view')" id="input-group-${idx}" label="备注" label-for="input-${idx}">
			<b-form-textarea id="textarea-${idx}" v-model="form['remarks']" placeholder="备注"></b-form-textarea>
		</b-form-group>
		</div>
</template>

<script>
	import mixin from "@/mixins/component.js";

	export default {
		mixins: [mixin],
		model: {
			prop: "form",
			event: "change"
		},
		props: {
			form: {
				type: Object,
				default: () => {
					return {

					}
				}
			}
		},
		data(){
			return {
				url_upload: "~/api/mall_users/upload?",
										        list_gender: "男,女",
					        // 类别选项列表
        list_category: [],
											}
		},
		methods: {
			// 下拉数据列表转换
			getDropList(e){
				let resultArr = [];
				if(e){
					let arr = e.split(",");
					arr.forEach(item => {
						resultArr.push({
							value: item,
							text: item
						})
					});
				}
				return resultArr;
			},
										      /**
       * 获取类别列表
       */
      async get_list_category() {
        let json = await this.$get("~/api/classification_information/get_list?");
        if(json.result && json.result.list){
          this.list_category = [];
          json.result.list.forEach(item => {
            this.list_category.push({
              value: item.category,
              text: item.category
            })
          });
        }
        else if(json.error){
          console.error(json.error);
        }
      },
								/**
			 * 上传图片
			 * @param {Object} file 文件对象
			 * @param {key} 保存键名
			 */
			uploadFile(file, key = "img") {
				var _this = this;
				var form = new FormData() // FormData 对象
				form.append('file', file[0]) // 文件对象
				this.$upload(this.url_upload, form, function(json) {
					if (json.result) {
						// _this.form[key] = json.result.url;
						_this.$delete(_this.form,key);
						_this.$set(_this.form,key,json.result.url);
						console.log(_this.form[key])
					} else {
						_this.$toast('上传失败！');
					}
				});
			},
		},
    created() {
					      this.get_list_category();
			    },
	mounted(){
								}
	}
</script>

<style>
</style>
