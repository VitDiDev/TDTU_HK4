package com.SpringCommerce.mapper;

import com.SpringCommerce.models.Customer;
import com.SpringCommerce.models.CustomerExample;
import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface CustomerMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    long countByExample(CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int deleteByExample(CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int deleteByPrimaryKey(Integer id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int insert(Customer row);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int insertSelective(Customer row);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    List<Customer> selectByExampleWithBLOBs(CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    List<Customer> selectByExample(CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    Customer selectByPrimaryKey(Integer id);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int updateByExampleSelective(@Param("row") Customer row, @Param("example") CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int updateByExampleWithBLOBs(@Param("row") Customer row, @Param("example") CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int updateByExample(@Param("row") Customer row, @Param("example") CustomerExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int updateByPrimaryKeySelective(Customer row);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int updateByPrimaryKeyWithBLOBs(Customer row);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table customer_new
     *
     * @mbg.generated Fri Apr 21 01:06:57 ICT 2023
     */
    int updateByPrimaryKey(Customer row);
}