<template>
  <el-main class="bg table_wrap">
    <el-form label-position="right" :model="query" class="form p_4" label-width="120">
      <el-row class="rows row1">

          
                                                              <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
                      <el-form-item label="标题">
                                                      <el-input v-model="query.title"></el-input>
                                                </el-form-item>
                    </el-col>
                                                                      <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
                      <el-form-item label="发布人">
                                                      <el-input v-model="query.publisher"></el-input>
                                                </el-form-item>
                    </el-col>
                                                                                                                                                                                                </el-row>
      <el-row class="rows row2">
      	<el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap search_btns">
         <el-col :xs="24" :sm="10" :lg="8" class="search_btn_1 search_btn_wrap_1 btns">
                              <el-button type="primary" @click="search()" class="search_btn_find">查询</el-button>
                <el-button @click="reset()" style="margin-right: 74px;" class="search_btn_reset">重置</el-button>
                                                     
            <el-button v-if="user_group == '管理员' || $check_action('/website_announcement/table','add') || $check_action('/website_announcement/view','add')" @click="$router.push('./view?')" class="add">添加</el-button>
						
            <el-button v-if="user_group == '管理员' || $check_action('/website_announcement/table','del') || $check_action('/website_announcement/view','del')" class="search_btn_del" type="danger" @click="delInfo()">删除</el-button>
                              <download-excel v-if="$check_option('/website_announcement/table','import_db')" class="export-excel-wrapper" :data="DetailsForm" :fields="json_fields" name="数据导入表格.xls" >
                  <el-button type="success">下载导入文档</el-button>
                </download-excel>
                <el-upload v-if="$check_option('/website_announcement/table','import_db')" action accept = ".xlsx, .xls" :auto-upload="false" :show-file-list="false" :on-change="handle_import">
                  <el-button type="primary">导入</el-button>
                </el-upload>
                        </el-col>
       
        </el-col>
      </el-row>
    </el-form>
    <el-table :data="list" @selection-change="selectionChange" @sort-change="$sortChange" style="width: 100%" id="dataTable">
                <el-table-column fixed type="selection" tooltip-effect="dark" width="55">
            </el-table-column>
                                                  <el-table-column prop="title" @sort-change="$sortChange" label="标题"
                               v-if="user_group == '管理员' || $check_field('get','title')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="publisher" @sort-change="$sortChange" label="发布人"
                               v-if="user_group == '管理员' || $check_field('get','publisher')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="release_time" @sort-change="$sortChange" label="发布时间"
                               v-if="user_group == '管理员' || $check_field('get','release_time')" min-width="200">
                                      <template slot-scope="scope">
                      {{ $toTime(scope.row["release_time"],"yyyy-MM-dd hh:mm:ss") }}
                    </template>
                                </el-table-column>
                                              <el-table-column prop="relevant_accessories" @sort-change="$sortChange" label="相关附件"
                               v-if="user_group == '管理员' || $check_field('get','relevant_accessories')" min-width="200">
                                      <template slot-scope="scope">
                      <a :href="$fullUrl(scope.row['relevant_accessories'])" target="_blank" style="color: rgb(64, 158, 255);">点击下载</a>
                    </template>
                                </el-table-column>
                                                                              <el-table-column prop="lower_multi_test" @sort-change="$sortChange" label="下多测试"
                               v-if="user_group == '管理员' || $check_field('get','lower_multi_test')" min-width="200">
                                </el-table-column>
                    
        
        
                
      <el-table-column sortable prop="create_time" label="创建时间" min-width="200">
        <template slot-scope="scope">
          {{ $toTime(scope.row["create_time"],"yyyy-MM-dd hh:mm:ss") }}
        </template>
      </el-table-column>

      <el-table-column sortable prop="update_time" label="更新时间" min-width="200">
        <template slot-scope="scope">
          {{ $toTime(scope.row["update_time"],"yyyy-MM-dd hh:mm:ss") }}
        </template>
      </el-table-column>

        
        
        
        
        

                <el-table-column fixed="right" label="操作" min-width="120" v-if="user_group == '管理员' || $check_action('/website_announcement/table','set') || $check_action('/website_announcement/view','set') || $check_action('/website_announcement/view','get') || $check_action('//table','add') || $check_action('//view','add')" >
        

      <template slot-scope="scope">
        <router-link class="el-button el-button--small is-plain el-button--success" style="margin: 5px !important;"
                     v-if="user_group == '管理员' || $check_action('/website_announcement/table','set') || $check_action('/website_announcement/view','set') || $check_action('/website_announcement/view','get')"
                                 :to="'./view?' + field + '=' + scope.row[field]"
                                 size="small">
          <span>详情</span>
        </router-link>
                                                                      <router-link v-if="user_group == '管理员' || $check_comment('/website_announcement/table')" class="el-button el-button--small is-plain el-button--primary"
                             :to="'../comment/table?size=10&page=1&source_table=website_announcement&source_field=' + field + '&source_id=' + scope.row[field]" size="small">
                  查看评论
                </router-link>
                              </template>
    </el-table-column>

    </el-table>

    <!-- 分页器 -->
    <div class="mt text_center">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
                     :current-page="query.page" :page-sizes="[7, 10, 30, 100]" :page-size="query.size"
                     layout="total, sizes, prev, pager, next, jumper" :total="count">
      </el-pagination>
    </div>
    <!-- /分页器 -->

                                                                                                                  
    <div class="modal_wrap" v-if="showModal">
      <div class="modal_box">
        <!-- <div class="modal_box_close" @click="closeModal">X</div> -->
        <p class="modal_box_title">重要提醒</p>
        <p class="modal_box_text">当前有数据达到预警值！</p>
        <div class="btn_box">
          <span @click="closeModal">取消</span>
          <span @click="closeModal">确定</span>
        </div>
      </div>
    </div>


  </el-main>
</template>
<script>
  import mixin from "@/mixins/page.js";
    import * as XLSX from 'xlsx/xlsx.mjs'
  
  export default {
    mixins: [mixin],
    data() {
      return {
        // 弹框
        showModal: false,
        // 获取数据地址
        url_get_list: "~/api/website_announcement/get_list?like=0",
        url_del: "~/api/website_announcement/del?",

        // 字段ID
        field: "website_announcement_id",

        // 查询
        query: {
          "size": 7,
          "page": 1,
                                                                      "title": "",
                                                                                                          "publisher": "",
                                                                                                                                                                                                          "login_time": "",
          "create_time": "",
          "orderby": `create_time desc`
        },

                  // 数据
        list: [],
                                          json_fields: {
                                                  "标题":'title',
                                  "发布人":'publisher',
                                  "发布时间":'release_time',
                                  "相关附件":'relevant_accessories',
                                  "详情":'details',
                                  "下多测试":'lower_multi_test',
                            },
            DetailsForm: [
              {
                                                              title:"文本类型",
                                            publisher:"文本类型",
                                            release_time:"日长类型",
                                            relevant_accessories:"文件类型",
                                            details:"编辑类型",
                                            lower_multi_test:"下多类型",
                                },
            ],
                                                                                                                                                                                                                                                                                                                                                                                                                        }
    },
    methods: {
      // 关闭弹框
      closeModal(){
        this.showModal = false;
      },
                
        
                                                                                                                                                                                                                
        
        
                  /**
           * 导入
           */
          readFile(file){//文件读取
            return new Promise(resolve => {
              let reader = new FileReader();
              reader.readAsBinaryString(file);//以二进制的方式读取
              reader.onload = ev =>{
                resolve(ev.target.result);
              }
            })
          },
          async handle_import(ev){
            let file = ev.raw;
            console.log(file)
            if(!file){
              console.log("文件打开失败")
              return ;
            }else{
              let data = await this.readFile(file);
              let workbook = XLSX.read(data,{ type: "binary"});//解析二进制格式数据
              let worksheet = workbook.Sheets[workbook.SheetNames[0]];//获取第一个Sheet
              let result = XLSX.utils.sheet_to_json(worksheet);//json数据格式
              result.forEach((item) => {
                // 将中文的键名替换成英文的
                for (let k in this.json_fields) {
                  let newKey = this.json_fields[k];
                  if (newKey) {
                    item[newKey] = item[k];
                    delete item[k];
                  }
                }
              });
              let _this = this;
                                  for (let i=0;i<result.length;i++){
                    let url = "~/api/website_announcement/add?";
                    await this.$post(url, result[i], function (json, status) {
                      console.log("提交结果：", json);
                      if (json.result) {
                        _this.$toast("操作成功", 'success');
                      } else if (json.error) {
                        _this.$toast(json.error.message, 'danger');
                      }
                    });
                  }
                            }
          },
        
                                                                                                                                                                                                                                      deleteRow(index, rows) {
        rows.splice(index, 1);
      }

    },
    created() {
                                                                                                                                                                                                                            }
  }
</script>

<style type="text/css">
  .bg {
    background: white;
  }

  .form.p_4 {
    padding: 1rem;
  }

  .form .el-input {
    width: initial;
  }

  .mt {
    margin-top: 1rem;
  }

  .text_center {
    text-align: center;
  }

  .float-right {
    float: right;
  }


  .modal_wrap{
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    background: rgba(0,0,0,0.5);
    z-index: 9999999999;
  }
  .modal_wrap .modal_box{
    width: 400px;
    height: 200px;
    background: url("../../assets/modal_bg.jpg") no-repeat center;
    background-size: cover;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -200px;
    margin-top: -100px;
    border-radius: 10px;
  }
  .modal_wrap .modal_box .modal_box_close{
    font-size: 20px;
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
  }
  .modal_wrap .modal_box .modal_box_title{
    text-align: center;
    font-size: 18px;
    margin: 16px auto;
    color: #fff;
    border-bottom: 1px solid rgba(117, 116, 116,0.5);
    padding-bottom: 16px;
    width: 356px;
  }
  .modal_wrap .modal_box .modal_box_text{
    text-align: center;
    font-size: 15px;
    color: #fff;
    margin-top: 25px;
  }
  .modal_wrap .modal_box .btn_box{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: 42px;
  }
  .modal_wrap .modal_box .btn_box span{
    display: inline-block;
    width: 80px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    border: 1px solid #ccc;
    font-size: 14px;
    cursor: pointer;
    color: #fff;
  }
  .modal_wrap .modal_box .btn_box span:nth-child(2){
    background: #409EFF;
    color: #fff;
    border-color: #409EFF;
    margin-left: 15px;
  }
</style>
