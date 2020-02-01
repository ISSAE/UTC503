/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lb.edu.isae.polynomer;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Acer
 */
public class PolynomeTest {
    static Polynome  instance;
    public PolynomeTest() {
        Integer[] c={1,2,3};
        instance = new Polynome(c);
    }
    
    @BeforeAll
    public static void setUpClass() {
        
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }

    /**
     * Test of P method, of class Polynome.
     */
    @Test
    public void testP() {
        System.out.println("P");
        int x = 0;
        //P(x)=x+2x^2+3x^3    
        int expResult = 1;
        int result = instance.P(x);
        assertEquals(expResult, result);
        expResult=6;
        result=instance.P(1);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of main method, of class Polynome.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        String[] args = null;
        Polynome.main(args);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
}
