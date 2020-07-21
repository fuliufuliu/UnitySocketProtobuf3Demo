package mysql

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"

	"fmt"
)

var (
	db *gorm.DB
)

func OpenDB() {
	fmt.Println("mysqldb->open db")
	//db1, err := gorm.Open("mysql", "mike:123456@tcp(localhost:3306)/poker?parseTime=true")
	db1, err := gorm.Open("mysql", "root:123456@tcp(localhost:3306)/e3b?parseTime=true")
	if err != nil {
		fmt.Println(err)
		panic("connect db error")
	}
	db = db1
}

func MysqlDB() *gorm.DB {
	return db
}
