import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

def test_TC01():
    # Khởi tạo trình duyệt Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    
    try:
        # Mở trang chủ
        driver.get("https://automationexercise.com")
        
        # Chờ title trang xuất hiện và kiểm tra có chứa 'Automation Exercise'
        WebDriverWait(driver, 10).until(EC.title_contains("Automation Exercise"))
        
        assert "Automation Exercise" in driver.title
        print("TC01 passed: Trang chủ tải thành công.")
    
    except Exception as e:
        print(f"TC01 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC01()

def test_TC02():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://automationexercise.com")
        
        # Đợi logo xuất hiện, logo trên trang có selector là img.logo hoặc kiểm tra src logo
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/static/images/home/logo.png']")))
        
        assert logo.is_displayed()
        print("TC02 passed: Logo hiển thị chính xác.")
    
    except Exception as e:
        print(f"TC02 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC02()

def test_TC03():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Đợi thanh menu chính xuất hiện
        nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar-nav')))
        
        # Kiểm tra thanh menu hiển thị
        assert nav.is_displayed()

        # Thêm kiểm tra số lượng menu (ví dụ 7 menu như trang hiện tại)
        menu_items = nav.find_elements(By.TAG_NAME, 'li')
        assert len(menu_items) >= 7

        print("TC03 passed: Thanh menu chính hiển thị đầy đủ.")
    
    except Exception as e:
        print(f"TC03 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC03()

def test_TC04():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Đợi banner slider xuất hiện, id 'slider-carousel' theo trang hiện tại
        banner = wait.until(EC.visibility_of_element_located((By.ID, 'slider-carousel')))
        
        assert banner.is_displayed()

        print("TC04 passed: Banner đầu trang hiển thị đầy đủ.")
    
    except Exception as e:
        print(f"TC04 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC04()

def test_TC05():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://automationexercise.com")
        
        # Click menu "Home"
        home_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_menu.click()
        
        # Chờ URL là trang chủ
        wait.until(EC.url_to_be("https://automationexercise.com/"))
        
        assert driver.current_url == "https://automationexercise.com/"
        print("TC05 passed: Click menu Home vẫn ở trang chủ.")
    
    except Exception as e:
        print(f"TC05 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC05()

def test_TC06():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://automationexercise.com")
        
        # Tìm menu Products chính xác hơn, scroll vào view trước khi click
        products_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", products_menu)
        products_menu.click()
        
        wait.until(EC.url_contains("/products"))
        assert "/products" in driver.current_url
        print("TC06 passed: Click menu Products điều hướng đúng trang sản phẩm.")
    
    except Exception as e:
        print(f"TC06 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC06()

def test_TC07():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Click menu "Cart"
        cart_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cart")))
        cart_menu.click()

        # Chờ URL chứa "/view_cart"
        wait.until(EC.url_contains("/view_cart"))

        assert "/view_cart" in driver.current_url
        print("TC07 passed: Click menu Cart điều hướng đúng trang giỏ hàng.")

    except Exception as e:
        print(f"TC07 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC07()

def test_TC08():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Click menu "Signup / Login"
        signup_login = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
        signup_login.click()

        # Chờ URL chứa "/login"
        wait.until(EC.url_contains("/login"))

        assert "/login" in driver.current_url
        print("TC08 passed: Click menu Signup / Login điều hướng đúng trang đăng nhập.")
    
    except Exception as e:
        print(f"TC08 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC08()

def test_TC09():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Click menu "Contact us"
        contact_us = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact us")))
        contact_us.click()

        # Chờ URL chứa "/contact_us"
        wait.until(EC.url_contains("/contact_us"))

        assert "/contact_us" in driver.current_url
        print("TC09 passed: Click menu Contact us điều hướng đúng trang liên hệ.")
    
    except Exception as e:
        print(f"TC09 failed: {e}")
    
    finally:
        driver.quit()

# Chạy thử
test_TC09()

def test_TC10():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Click logo
        logo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[src='/static/images/home/logo.png']")))
        logo.click()

        # Chờ URL vẫn là trang chủ
        wait.until(EC.url_to_be("https://automationexercise.com/"))

        assert driver.current_url == "https://automationexercise.com/"
        print("TC10 passed: Click logo trên trang chủ vẫn load lại trang chủ.")

    except Exception as e:
        print(f"TC10 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC10()

def test_TC11():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới Category
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)

        # Click mở WOMEN (liên kết a có href="#Women")
        women_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Women"]')
        ))
        women_toggle.click()

        # Đợi menu con mở và click "Dress" bên trong (dùng contains + normalize-space)
        dress_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Women"]//a[contains(normalize-space(text()), "Dress")]')
        ))
        dress_link.click()

        # Kiểm tra header trang sản phẩm hiển thị danh mục WOMEN - DRESS
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Women - Dress Products')]")
        ))
        assert header.is_displayed()

        print("TC11 passed: Trang sản phẩm hiển thị danh mục WOMEN - DRESS đúng.")

    except Exception as e:
        print(f"TC11 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC11()

def test_TC12():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới Category
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)

        # Click mở WOMEN trong Category
        women_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Women"]')
        ))
        women_toggle.click()

        # Click vào TOPS trong menu WOMEN (dùng contains và normalize-space để xử lý khoảng trắng)
        tops_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Women"]//a[contains(normalize-space(text()), "Tops")]')
        ))
        tops_link.click()

        # Kiểm tra header trang sản phẩm chứa "Women - Tops Products"
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Women - Tops Products')]")
        ))
        assert header.is_displayed()

        print("TC12 passed: Trang sản phẩm hiển thị danh mục WOMEN - TOPS đúng.")

    except Exception as e:
        print(f"TC12 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC12()

def test_TC13():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới Category
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)

        # Click mở WOMEN trong Category
        women_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Women"]')
        ))
        women_toggle.click()

        # Click vào Saree trong menu WOMEN (dùng contains + normalize-space)
        saree_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Women"]//a[contains(normalize-space(text()), "Saree")]')
        ))
        saree_link.click()

        # Kiểm tra header trang sản phẩm chứa "Women - Saree Products"
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Women - Saree Products')]")
        ))
        assert header.is_displayed()

        print("TC13 passed: Trang sản phẩm hiển thị danh mục WOMEN - SAREE đúng.")

    except Exception as e:
        print(f"TC13 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC13()

def test_TC14():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Mở danh mục
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)

        # Mở menu MEN
        men_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Men"]')
        ))
        men_toggle.click()

        # Click vào Tshirts
        tshirts_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Men"]//a[contains(normalize-space(text()), "Tshirts")]')
        ))
        tshirts_link.click()

        # Kiểm tra header đúng
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Men - Tshirts Products')]")
        ))
        assert header.is_displayed()
        print("TC14 passed: Trang sản phẩm hiển thị danh mục MEN - TSHIRTS đúng.")

    except Exception as e:
        print(f"TC14 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC14()

def test_TC15():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Mở danh mục
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)

        # Mở menu MEN
        men_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Men"]')
        ))
        men_toggle.click()

        # Click vào Jeans
        jeans_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Men"]//a[contains(normalize-space(text()), "Jeans")]')
        ))
        jeans_link.click()

        # Kiểm tra header đúng
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Men - Jeans Products')]")
        ))
        assert header.is_displayed()
        print("TC15 passed: Trang sản phẩm hiển thị danh mục MEN - JEANS đúng.")

    except Exception as e:
        print(f"TC15 failed: {e}")

    finally:
        driver.quit()

# Chạy thử
test_TC15()

def test_TC16():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới Category và mở menu Kids
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)
        kids_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Kids"]')
        ))
        kids_toggle.click()

        # Click vào Dress trong menu KIDS
        dress_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Kids"]//a[contains(normalize-space(text()), "Dress")]')
        ))
        dress_link.click()

        # Kiểm tra header trang sản phẩm
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Kids - Dress Products')]")
        ))
        assert header.is_displayed()
        print("TC16 passed: Trang sản phẩm hiển thị danh mục KIDS - DRESS đúng.")

    except Exception as e:
        print(f"TC16 failed: {e}")
    finally:
        driver.quit()

# Chạy thử
test_TC16()

def test_TC17():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới Category và mở menu Kids
        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".left-sidebar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", category)
        kids_toggle = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-toggle="collapse"][href="#Kids"]')
        ))
        kids_toggle.click()

        # Click vào Tops & Shirts trong menu KIDS
        tops_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="Kids"]//a[contains(normalize-space(text()), "Tops & Shirts")]')
        ))
        tops_link.click()

        # Kiểm tra header trang sản phẩm
        header = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Kids - Tops & Shirts Products')]")
        ))
        assert header.is_displayed()
        print("TC17 passed: Trang sản phẩm hiển thị danh mục KIDS - TOPS & SHIRTS đúng.")

    except Exception as e:
        print(f"TC17 failed: {e}")
    finally:
        driver.quit()

# Chạy thử
test_TC17()

def test_TC18():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới mục Brands
        brands_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Brands']")))
        driver.execute_script("arguments[0].scrollIntoView();", brands_title)

        # Click vào Polo
        polo_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/brand_products/Polo']")))
        polo_link.click()

        # Chờ URL chuyển đến Polo
        wait.until(EC.url_contains("/brand_products/Polo"))
        assert "/brand_products/Polo" in driver.current_url

        print("TC18 passed: Trang sản phẩm thuộc thương hiệu POLO hiển thị đúng.")

    except Exception as e:
        import traceback
        print("TC18 failed:")
        traceback.print_exc()

    finally:
        driver.quit()

test_TC18()

def test_TC19():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        brand = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/brand_products/H&M']")))
        brand.click()

        wait.until(EC.url_contains("/brand_products/H&M"))
        assert "/brand_products/H&M" in driver.current_url
        print("TC19 passed: Đã hiển thị sản phẩm thuộc brand H&M.")

    except Exception as e:
        print(f"TC19 failed: {e}")

    finally:
        driver.quit()

test_TC19()

def test_TC20():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        brand = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/brand_products/Madame']")))
        brand.click()

        wait.until(EC.url_contains("/brand_products/Madame"))
        assert "/brand_products/Madame" in driver.current_url
        print("TC20 passed: Đã hiển thị sản phẩm thuộc brand MADAME.")

    except Exception as e:
        print(f"TC20 failed: {e}")

    finally:
        driver.quit()

test_TC20()

def test_TC21():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn xuống để Brands chắc chắn hiện
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # XPath tìm <a> có href chứa "Mast" và "Harbour"
        brand_xpath = "//a[contains(@href, 'Mast') and contains(@href, 'Harbour')]"

        brand = wait.until(EC.element_to_be_clickable((By.XPATH, brand_xpath)))
        brand.click()

        wait.until(EC.url_contains("/brand_products/Mast"))
        assert "/brand_products/Mast" in driver.current_url

        print("TC21 passed: Đã hiển thị sản phẩm thuộc brand MAST & HARBOUR.")

    except Exception:
        print("TC21 failed:")
        traceback.print_exc()

    finally:
        driver.quit()

test_TC21()

def test_TC22():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        brand = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/brand_products/Babyhug']")))
        brand.click()

        wait.until(EC.url_contains("/brand_products/Babyhug"))
        assert "/brand_products/Babyhug" in driver.current_url
        print("TC22 passed: Đã hiển thị sản phẩm thuộc brand BABYHUG.")

    except Exception as e:
        print(f"TC22 failed: {e}")

    finally:
        driver.quit()

test_TC22()

def test_TC23():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 15)  # tăng thời gian chờ

    try:
        driver.get("https://automationexercise.com")

        # Cuộn xuống để phần Brands chắc chắn hiển thị
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Dùng contains để tránh lỗi nếu href encoding khác
        brand_xpath = "//a[contains(@href, 'Allen') and contains(@href, 'Solly') and contains(@href, 'Junior')]"
        brand = wait.until(EC.element_to_be_clickable((By.XPATH, brand_xpath)))
        brand.click()

        # Chờ URL chuyển đúng
        wait.until(EC.url_contains("/brand_products/Allen%20Solly%20Junior"))
        assert "/brand_products/Allen%20Solly%20Junior" in driver.current_url

        print("TC23 passed: Đã hiển thị sản phẩm thuộc brand ALLEN SOLLY JUNIOR.")

    except Exception:
        print("TC23 failed:")
        traceback.print_exc()

    finally:
        driver.quit()

test_TC23()

def test_TC24():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 15)  # tăng timeout

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới phần Brands
        brands_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Brands']")))
        driver.execute_script("arguments[0].scrollIntoView();", brands_title)

        # Click vào link "Kookie Kids"
        kookie_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/brand_products/Kookie Kids']")))
        kookie_link.click()

        wait.until(EC.url_contains("/brand_products/Kookie%20Kids"))
        assert "/brand_products/Kookie%20Kids" in driver.current_url

        print("TC24 passed: Trang sản phẩm thuộc thương hiệu KOOKIE KIDS hiển thị đúng.")

    except Exception as e:
        import traceback
        print("TC24 failed:")
        traceback.print_exc()

    finally:
        driver.quit()

test_TC24()

def test_TC25():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        brand = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/brand_products/Biba']")))
        brand.click()

        wait.until(EC.url_contains("/brand_products/Biba"))
        assert "/brand_products/Biba" in driver.current_url
        print("TC25 passed: Đã hiển thị sản phẩm thuộc brand BIBA.")

    except Exception as e:
        print(f"TC25 failed: {e}")

    finally:
        driver.quit()

test_TC25()

def test_TC26():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn tới phần sản phẩm Featured Items (hoặc Category tùy theo trang)
        products_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Category' or text()='Recommended Items' or text()='Features Items']")))
        driver.execute_script("arguments[0].scrollIntoView();", products_section)

        # Lấy tất cả sản phẩm trong phần đó
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".features_items .col-sm-4")))

        # Chọn ngẫu nhiên 1 sản phẩm
        chosen_product = random.choice(products)

        # Hover chuột vào sản phẩm đã chọn
        action.move_to_element(chosen_product).perform()

        # Tìm nút View Product nằm bên trong sản phẩm đó (dùng XPath tương đối)
        view_product_button = chosen_product.find_element(By.XPATH, ".//a[contains(text(),'View Product')]")

        if view_product_button.is_displayed():
            print("TC26 passed: Nút 'View Product' hiển thị khi hover vào sản phẩm.")
        else:
            print("TC26 failed: Nút 'View Product' không hiển thị khi hover vào sản phẩm.")

    except TimeoutException:
        print("TC26 failed: Không tìm thấy sản phẩm hoặc nút 'View Product'.")
    except Exception as e:
        print(f"TC26 failed: {e}")

    finally:
        driver.quit()

test_TC26()

def test_TC27():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn xuống phần sản phẩm
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Lấy tất cả sản phẩm trong danh sách
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.features_items div.product-image-wrapper")))

        # Chọn ngẫu nhiên 1 sản phẩm
        chosen_product = random.choice(products)

        # Lấy tên sản phẩm trên trang chủ
        product_name = chosen_product.find_element(By.CSS_SELECTOR, "div.productinfo p").text.strip()

        # Click vào nút View Product
        view_product_btn = chosen_product.find_element(By.XPATH, ".//a[text()='View Product']")
        view_product_btn.click()

        # Chờ trang chi tiết tải xong
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-information h2")))

        # Lấy tên sản phẩm trên trang chi tiết
        detail_name = driver.find_element(By.CSS_SELECTOR, "div.product-information h2").text.strip()

        # So sánh tên sản phẩm
        if product_name == detail_name:
            print(f"TC27 passed: Tên sản phẩm '{product_name}' khớp giữa trang chủ và trang chi tiết.")
        else:
            print(f"TC27 failed: Tên sản phẩm không khớp.\nTrang chủ: {product_name}\nTrang chi tiết: {detail_name}")

    except Exception as e:
        print("TC27 failed due to exception:")
        traceback.print_exc()

    finally:
        driver.quit()

test_TC27_random_product()

def test_TC28():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")

        # Cuộn đến phần sản phẩm (Featured Items)
        products_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Category' or text()='Features Items' or text()='Recommended Items']")))
        driver.execute_script("arguments[0].scrollIntoView();", products_section)

        # Lấy danh sách tất cả sản phẩm
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".features_items .col-sm-4")))

        all_have_view_product = True

        # Duyệt từng sản phẩm kiểm tra có nút "View Product" không
        for idx, product in enumerate(products, start=1):
            try:
                view_button = product.find_element(By.XPATH, ".//a[contains(text(),'View Product')]")
                if not view_button.is_displayed():
                    print(f"TC28 failed: Sản phẩm thứ {idx} không hiển thị nút 'View Product'.")
                    all_have_view_product = False
            except NoSuchElementException:
                print(f"TC28 failed: Sản phẩm thứ {idx} không có nút 'View Product'.")
                all_have_view_product = False

        if all_have_view_product:
            print("TC28 passed: Tất cả sản phẩm đều có nút 'View Product'.")

    except TimeoutException:
        print("TC28 failed: Không tìm thấy phần sản phẩm hoặc danh sách sản phẩm.")
    except Exception as e:
        print(f"TC28 failed: {e}")

    finally:
        driver.quit()

test_TC28()

def test_TC29():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://automationexercise.com")
    driver.maximize_window()

    try:
        # Cuộn tới phần danh sách sản phẩm
        products_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Category']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", products_title)
        time.sleep(1)

        # Chờ và lấy danh sách sản phẩm
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".features_items .col-sm-4")))
        if not products:
            print("TC29 failed: Không tìm thấy sản phẩm nào.")
            return

        # Chọn sản phẩm ngẫu nhiên
        chosen_product = random.choice(products)

        # Cuộn vào đúng sản phẩm và hover
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", chosen_product)
        ActionChains(driver).move_to_element(chosen_product).perform()
        time.sleep(1)

        # Click nút Add to cart qua ActionChains để tránh bị chặn
        add_button = chosen_product.find_element(By.XPATH, ".//a[contains(text(),'Add to cart')]")
        ActionChains(driver).move_to_element(add_button).click().perform()

        # Đợi popup hiển thị
        popup = wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
        time.sleep(1)

        # Kiểm tra 2 nút View Cart và Continue Shopping
        view_cart = popup.find_element(By.XPATH, ".//a[@href='/view_cart']")
        continue_shopping = popup.find_element(By.XPATH, ".//button[contains(text(),'Continue Shopping')]")

        if view_cart.is_displayed() and continue_shopping.is_displayed():
            print("✅ TC29 passed: Popup hiển thị đúng với 2 nút.")
        else:
            print("❌ TC29 failed: Một trong hai nút không hiển thị.")

    except Exception as e:
        print(f"❌ TC29 failed: {e}")
    finally:
        time.sleep(2)
        driver.quit()

test_TC29()

def test_TC30():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://automationexercise.com")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".features_items .col-sm-4")))
        random_product = random.choice(products)

        product_name = random_product.find_element(By.TAG_NAME, "p").text
        product_price = random_product.find_element(By.TAG_NAME, "h2").text

        add_button = random_product.find_element(By.CLASS_NAME, "add-to-cart")
        driver.execute_script("arguments[0].click();", add_button)

        view_cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_btn.click()

        cart_product_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_description"))).text
        cart_product_price = driver.find_element(By.CLASS_NAME, "cart_price").text
        cart_quantity = driver.find_element(By.CLASS_NAME, "cart_quantity").text

        if product_name in cart_product_name and product_price in cart_product_price and cart_quantity == "1":
            print("✅ TC30 passed: Sản phẩm được thêm đúng vào giỏ hàng")
        else:
            print("❌ TC30 failed: Dữ liệu trong giỏ hàng không khớp")
            print(f"Tên: {product_name} → {cart_product_name}")
            print(f"Giá: {product_price} → {cart_product_price}")
            print(f"Số lượng: {cart_quantity}")

    except Exception as e:
        print(f"❌ TC30 failed: {e}")

    finally:
        time.sleep(3)
        driver.quit()
        
test_TC30()

def test_TC31():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        driver.get("https://automationexercise.com")
        time.sleep(2)

        products = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
        if not products:
            raise Exception("Không tìm thấy sản phẩm nào!")

        random_product = random.choice(products)
        driver.execute_script("arguments[0].scrollIntoView(true);", random_product)
        time.sleep(1)
        add_to_cart_button = random_product.find_element(By.XPATH, ".//a[contains(text(),'Add to cart')]")
        add_to_cart_button.click()
        time.sleep(2)

        continue_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]")
        continue_btn.click()
        time.sleep(2)

        popup_visible = False
        try:
            modal = driver.find_element(By.ID, "cartModal")
            popup_visible = modal.is_displayed()
        except:
            popup_visible = False

        current_url = driver.current_url
        if not popup_visible and "automationexercise.com" in current_url:
            print("✅ TC31 passed: Popup đóng, người dùng vẫn ở lại trang hiện tại.")
        else:
            print("❌ TC31 failed: Popup chưa đóng hoặc bị chuyển trang.")
    except Exception as e:
        print(f"❌ TC31 failed: {str(e)}")
    finally:
        time.sleep(2)
        driver.quit()
        
test_TC31()

def main():
    test_funcs = [
    test_TC01, test_TC02, test_TC03, test_TC04, test_TC05, test_TC06, test_TC07,
    test_TC08, test_TC09, test_TC10, test_TC11, test_TC12, test_TC13, test_TC14,
    test_TC15, test_TC16, test_TC17, test_TC18, test_TC19, test_TC20, test_TC21,
    test_TC22, test_TC23, test_TC24, test_TC25, test_TC26, test_TC27, test_TC28,
    test_TC29, test_TC30, test_TC31
    ]  
    total = len(test_funcs)
    passed = 0
    failed = 0

    start_time = time.time()
    for func in test_funcs:
        if func():
            passed += 1
        else:
            failed += 1
    end_time = time.time()

    print("\n===== Test Summary =====")
    print(f"Total test cases: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

