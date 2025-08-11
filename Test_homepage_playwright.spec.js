const { test, expect } = require('@playwright/test');

test.describe('Kiểm tra trang chủ Automation Exercise', () => {

  test.setTimeout(60000);
  
  test.beforeEach(async ({ page }) => {
    await page.goto('https://automationexercise.com', { timeout: 60000, waitUntil: 'domcontentloaded' });
  });

  // ========== TC01 ==========
  test('TC01 - Kiểm tra trang chủ tải thành công', async ({ page }) => {
    await expect(page).toHaveTitle(/Automation Exercise/);
  });

  // ========== TC02 ==========
  test('TC02 - Kiểm tra logo được hiển thị', async ({ page }) => {
    await expect(page.locator("img[src='/static/images/home/logo.png']")).toBeVisible();
  });

  // ========== TC03 ==========
  test('TC03 - Kiểm tra thanh menu chính hiển thị và có ít nhất 7 mục', async ({ page }) => {
    const menu = page.locator('.navbar-nav');
    await expect(menu).toBeVisible();
    const count = await menu.locator('li').count();
    expect(count).toBeGreaterThanOrEqual(7);
  });

  // ========== TC04 ==========
  test('TC04 - Kiểm tra banner đầu trang hiển thị', async ({ page }) => {
    await expect(page.locator('#slider-carousel')).toBeVisible();
  });

  // ========== TC05 ==========
  test('TC05 - Click menu Home vẫn ở trang chủ', async ({ page }) => {
    await page.getByRole('link', { name: 'Home' }).click();
    await expect(page).toHaveURL('https://automationexercise.com/');
  });

  // ========== TC06 ==========
  test('TC06 - Click menu Products điều hướng đúng trang sản phẩm', async ({ page }) => {
    await page.getByRole('link', { name: 'Products' }).click();
    await expect(page).toHaveURL(/\/products/);
  });

  // ========== TC07 ==========
  test('TC07 - Click menu Cart điều hướng đúng trang giỏ hàng', async ({ page }) => {
    await page.getByRole('link', { name: 'Cart' }).click();
    await expect(page).toHaveURL(/\/view_cart/);
  });

  // ========== TC08 ==========
  test('TC08 - Click menu Signup / Login điều hướng đúng trang đăng nhập', async ({ page }) => {
    await page.getByRole('link', { name: 'Signup / Login' }).waitFor({ state: 'visible' });
    await page.getByRole('link', { name: 'Signup / Login' }).click();
    await expect(page).toHaveURL(/\/login/);
  });

  test('TC09 - Click menu Contact us điều hướng đúng trang liên hệ', async ({ page }) => {
	await page.getByRole('link', { name: 'Contact us' }).waitFor({ state: 'visible' });
	await page.getByRole('link', { name: 'Contact us' }).click({ force: true });

	// Đợi URL đúng với trang Contact us (có thể có query/hash)
	await page.waitForURL(/\/contact_us(\?.*)?(#.*)?$/, { timeout: 10000 });

	// Kiểm tra URL chứa contact_us
	await expect(page).toHaveURL(/\/contact_us(\?.*)?(#.*)?$/);
  });

  // ========== TC10 ==========
  test('TC10 - Click logo trên trang chủ vẫn load lại trang chủ', async ({ page }) => {
    await page.locator("img[src='/static/images/home/logo.png']").click();
    await expect(page).toHaveURL('https://automationexercise.com/');
  });

  // Hàm mở category
  async function openCategory(page, category, sub) {
    await page.locator('.left-sidebar').scrollIntoViewIfNeeded();
    await page.locator(`a[href="#${category}"]`).click();
    await page.locator(`#${category} a`, { hasText: sub }).click();
  }

  // ========== TC11 ~ TC17 ==========
  test('TC11 - WOMEN → Dress', async ({ page }) => {
    await openCategory(page, 'Women', 'Dress');
	await expect(page.getByRole('heading', { name: 'Women - Dress Products' })).toBeVisible();
  });

  test('TC12 - WOMEN → Tops', async ({ page }) => {
    await openCategory(page, 'Women', 'Tops');
    await expect(page.getByRole('heading', { name: 'Women - Tops Products' })).toBeVisible();
  });

  test('TC13 - WOMEN → Saree', async ({ page }) => {
    await openCategory(page, 'Women', 'Saree');
    await expect(page.getByRole('heading', { name: 'Women - Saree Products' })).toBeVisible();
  });

  test('TC14 - MEN → Tshirts', async ({ page }) => {
    await openCategory(page, 'Men', 'Tshirts');
    await expect(page.getByRole('heading', { name: 'Men - Tshirts Products' })).toBeVisible();
  });

  test('TC15 - MEN → Jeans', async ({ page }) => {
    await openCategory(page, 'Men', 'Jeans');
    await expect(page.getByRole('heading', { name: 'Men - Jeans Products' })).toBeVisible();
  });

  test('TC16 - KIDS → Dress', async ({ page }) => {
    await openCategory(page, 'Kids', 'Dress');
    await expect(page.getByRole('heading', { name: 'Kids - Dress Products' })).toBeVisible();
  });

  test('TC17 - KIDS → Tops & Shirts', async ({ page }) => {
    await openCategory(page, 'Kids', 'Tops & Shirts');
    await expect(page.getByRole('heading', { name: 'Kids - Tops & Shirts Products' })).toBeVisible();
  });

  // ========== TC18 ~ TC25 ==========
  const brands = [
    { tc: 18, name: 'Polo' },
    { tc: 19, name: 'H&M' },
    { tc: 20, name: 'Madame' },
    { tc: 21, name: 'Mast & Harbour', partial: 'Mast' },
    { tc: 22, name: 'Babyhug' },
    { tc: 23, name: 'Allen Solly Junior' },
    { tc: 24, name: 'Kookie Kids' },
    { tc: 25, name: 'Biba' },
  ];

  for (const b of brands) {
    test(`TC${b.tc} - Hiển thị sản phẩm brand ${b.name}`, async ({ page }) => {
      // Scroll brands sidebar vào view
      await page.locator('.brands_products').scrollIntoViewIfNeeded();

      // Tìm link brand theo text, tránh dùng href do có khoảng trắng
      const brandLink = page.locator('a', { hasText: b.name });

      // Chờ link xuất hiện
      await brandLink.waitFor({ state: 'visible', timeout: 5000 });

      // Click vào brand
      await brandLink.click();

      // Kiểm tra URL chứa brand partial hoặc tên đầy đủ (thay dấu cách thành dấu - cho URL)
      const expectedPartial = (b.partial || b.name).replace(/ /g, '%20');
      await expect(page).toHaveURL(new RegExp(`/brand_products/${expectedPartial}`));
    });
  }

  // ========== TC26 ==========
  test('TC26 - Nút View Product hiển thị khi hover sản phẩm ngẫu nhiên', async ({ page }) => {
    const products = await page.locator('.features_items .col-sm-4').all();
    const randomIndex = Math.floor(Math.random() * products.length);
    await products[randomIndex].hover();
    await expect(products[randomIndex].locator('a', { hasText: 'View Product' })).toBeVisible();
  });

  // ========== TC27 ==========
  test('TC27 - Tên sản phẩm khớp giữa trang chủ và chi tiết', async ({ page }) => {
    const products = await page.locator('.features_items .product-image-wrapper').all();
    const randomIndex = Math.floor(Math.random() * products.length);
    const chosen = products[randomIndex];
    const name = (await chosen.locator('.productinfo p').innerText()).trim();
    await chosen.locator('a', { hasText: 'View Product' }).click();
    const detailName = (await page.locator('.product-information h2').innerText()).trim();
    expect(detailName).toBe(name);
  });

  // ========== TC28 ==========
  test('TC28 - Tất cả sản phẩm có nút View Product', async ({ page }) => {
    const products = await page.locator('.features_items .col-sm-4').all();
    for (const p of products) {
      await expect(p.locator('a', { hasText: 'View Product' })).toBeVisible();
    }
  });

  // ========== TC29 ==========
  test('TC29 - Popup Add to Cart hiển thị khi thêm sản phẩm', async ({ page }) => {
    const products = await page.locator('.features_items .col-sm-4').all();
    const randomIndex = Math.floor(Math.random() * products.length);
    const chosen = products[randomIndex];
    await chosen.hover();
    await chosen.locator('a.add-to-cart').first().click();
    await expect(page.locator('#cartModal')).toBeVisible();
    await expect(page.locator('#cartModal a[href="/view_cart"]')).toBeVisible();
    await expect(page.locator('#cartModal button', { hasText: 'Continue Shopping' })).toBeVisible();
  });

  // ========== TC30 ==========
  test('TC30 - Thêm sản phẩm vào giỏ và kiểm tra', async ({ page }) => {
    const products = await page.locator('.features_items .col-sm-4').all();
    const randomIndex = Math.floor(Math.random() * products.length);
    const chosen = products[randomIndex];

    const name = (await chosen.locator('.productinfo p').innerText()).trim();
    const price = (await chosen.locator('.productinfo h2').innerText()).trim();

    // Tắt animation popup modal tránh lỗi trên Webkit
    await page.addStyleTag({ content: `
      #cartModal {
        transition: none !important;
        animation: none !important;
      }
    `});

    await chosen.locator('.productinfo a.add-to-cart').click();

    // Chờ modal popup hiển thị (visible = display khác none, opacity > 0)
    await page.waitForSelector('#cartModal', { state: 'visible', timeout: 10000 });

    // Chờ nút View Cart hiện và click
    const viewCartBtn = page.locator('#cartModal a', { hasText: 'View Cart' });
    await expect(viewCartBtn).toBeVisible({ timeout: 5000 });
    await viewCartBtn.click();

    // Chờ trang giỏ hàng tải xong
    await expect(page).toHaveURL(/\/view_cart/);

    // Kiểm tra thông tin trong giỏ hàng
    const cartName = (await page.locator('.cart_description a[href*="/product_details"]').innerText()).trim();
    const cartPrice = (await page.locator('.cart_price').innerText()).trim();
    const quantity = (await page.locator('.cart_quantity button').innerText()).trim();

    expect(cartName).toBe(name);
    expect(cartPrice).toBe(price);
    expect(quantity).toBe('1');
  });

  // ========== TC31 ==========
  test('TC31 - Đóng popup Continue Shopping không chuyển trang', async ({ page }) => {
    // Tắt animation modal để tránh lỗi chờ popup trên Webkit
    await page.addStyleTag({ content: `
      #cartModal {
        transition: none !important;
        animation: none !important;
      }
    `});

    const products = await page.locator('.product-image-wrapper').all();
    const randomIndex = Math.floor(Math.random() * products.length);
    const chosen = products[randomIndex];

    await chosen.hover();
    await chosen.locator('a.add-to-cart').first().click();

    // Chờ modal popup có class 'show' (Bootstrap modal đang mở)
    await page.waitForSelector('#cartModal.show', { timeout: 10000 });

    // Click nút Continue Shopping
    await page.locator('#cartModal button', { hasText: 'Continue Shopping' }).click();

    // Chờ modal ẩn đi (bị remove class 'show' hoặc bị ẩn)
    await page.waitForSelector('#cartModal', { state: 'hidden', timeout: 10000 });

    // Kiểm tra URL không đổi, vẫn ở trang chính
    await expect(page).toHaveURL(/automationexercise\.com/);
  });

});
