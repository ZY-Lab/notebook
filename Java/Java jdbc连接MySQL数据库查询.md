#使用JDBC查询mysql数据库示例
    import java.sql.*;
    
    public class test1 {
        public static void main(String[] args) {
    
            /**
             * 使用JDBC查询mysql数据库示例
             */
             
            try {
                // 1.反射获取mysql驱动实例
                Class.forName("com.mysql.jdbc.Driver");
            } catch (ClassNotFoundException e) {
                System.out.println("找不到驱动程序类，加载驱动失败！");
                e.printStackTrace();
            }
    
            String url = "jdbc:mysql://127.0.0.1:3306/show";
            String username = "root";
            String password = "root";
            
            try {
                // 2.驱动实例->Connection
                Connection conn = DriverManager.getConnection(url, username, password);
                
                // 3.Connection->Statement
                Statement stmt = conn.createStatement();
                
                // 4.Statement->ResultSet
                String sql = "select * from member_user";
                ResultSet rs = stmt.executeQuery(sql);
        
                // 5.通过ResultSet获取数据
                while (rs.next()) {
                    String id = rs.getString("id");
                    String name = rs.getString("password");
                    String score = rs.getString("username");
                    String sex = rs.getString("head_img");
                    String theClass = rs.getString("birthday");
                    System.out.println(id + "--" + name + "--" + score + "--" + sex + "--" + theClass);
    
                }
        
                // 6.依次关闭ResultSet,Statement,Connection
                if (rs != null) {
                    try {
                        rs.close();
                    } catch (SQLException e) {
                        System.out.println("ResultSet关闭时出现错误！");
                        e.printStackTrace();
                    }
                }
                if (stmt != null) {
                    try {
                        stmt.close();
                    } catch (SQLException e) {
                        System.out.println("Statement关闭时出现错误！");
                        e.printStackTrace();
                    }
                }
                if (conn != null) {
                    try {
                        conn.close();
                    } catch (SQLException e) {
                        System.out.println("Connection关闭时出现错误！");
                        e.printStackTrace();
                    }
                }
    
            } catch (SQLException e) {
                System.out.println("数据库连接失败！");
                e.printStackTrace();
            }
        }
    }
