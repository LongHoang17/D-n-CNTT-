describe('Kiểm tra trang chủ Automation Exercise', () => {

  beforeEach(() => {
    // Mở trang chủ trước mỗi bài kiểm thử
    cy.visit('https://automationexercise.com');
  });


  it('TC01 - Kiểm tra trang chủ tải thành công', () => {
    cy.title().should('include', 'Automation Exercise');
  });

  it('TC02 - Kiểm tra logo được hiển thị', () => {
    cy.get("img[src='/static/images/home/logo.png']").should('be.visible');
  });

  it('TC03 - Kiểm tra thanh menu chính hiển thị và có ít nhất 7 mục', () => {
    // Kiểm tra thanh menu chính có hiển thị
    cy.get('.navbar-nav').should('be.visible');

    // Kiểm tra có ít nhất 7 mục trong menu
    cy.get('.navbar-nav > li').its('length').should('be.gte', 7);
  });

  it('TC04 - Kiểm tra banner đầu trang có ID slider-carousel hiển thị', () => {
    cy.get('#slider-carousel').should('be.visible');
  });

  it('TC05 - Kiểm tra click vào menu Home vẫn ở trang chủ', () => {
    cy.contains('a', 'Home').click();
    cy.url().should('eq', 'https://automationexercise.com/');
  });
  
  it('TC06 - Click menu Products điều hướng đúng trang sản phẩm', () => {
    // Scroll đến menu Products và click
    cy.contains('a', 'Products').scrollIntoView().click()
    // Kiểm tra URL có chứa /products
    cy.url().should('include', '/products')
  });

  it('TC07 - Click menu Cart điều hướng đúng trang giỏ hàng', () => {
    cy.contains('a', 'Cart').click()
    cy.url().should('include', '/view_cart')
  });

  it('TC08 - Click menu Signup / Login điều hướng đúng trang đăng nhập', () => {
    cy.contains('a', 'Signup / Login').click()
    cy.url().should('include', '/login')
  });

  it('TC09 - Click menu Contact us điều hướng đúng trang liên hệ', () => {
    cy.contains('a', 'Contact us').click()
    cy.url().should('include', '/contact_us')
  });
  
  it('TC10 - Click logo trên trang chủ vẫn load lại trang chủ', () => {
    cy.get("img[src='/static/images/home/logo.png']").click()
    cy.url().should('eq', 'https://automationexercise.com/')
  })

  it('TC11 - Mở Category WOMEN và chọn Dress, kiểm tra trang sản phẩm hiển thị đúng', () => {
    // Cuộn tới Category
    cy.get('.left-sidebar').scrollIntoView()
    // Mở menu WOMEN
    cy.get('a[data-toggle="collapse"][href="#Women"]').click()
    // Click Dress trong WOMEN
    cy.get('#Women a').contains('Dress').click()
    // Kiểm tra header trang sản phẩm
    cy.get('h2').contains('Women - Dress Products').should('be.visible')
  });

  it('TC12 - Mở Category WOMEN và chọn Tops, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.get('.left-sidebar').scrollIntoView()
    cy.get('a[data-toggle="collapse"][href="#Women"]').click()
    cy.get('#Women a').contains('Tops').click()
    cy.get('h2').contains('Women - Tops Products').should('be.visible')
  });

  it('TC13 - Mở Category WOMEN và chọn Saree, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.get('.left-sidebar').scrollIntoView()
    cy.get('a[data-toggle="collapse"][href="#Women"]').click()
    cy.get('#Women a').contains('Saree').click()
    cy.get('h2').contains('Women - Saree Products').should('be.visible')
  });
  
  it('TC14 - Mở danh mục MEN và chọn Tshirts, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.get('.left-sidebar').scrollIntoView()
    cy.get('a[data-toggle="collapse"][href="#Men"]').click()
    cy.get('#Men a').contains('Tshirts').click()
    cy.get('h2').contains('Men - Tshirts Products').should('be.visible')
  });

  it('TC15 - Mở danh mục MEN và chọn Jeans, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.get('.left-sidebar').scrollIntoView()
    cy.get('a[data-toggle="collapse"][href="#Men"]').click()
    cy.get('#Men a').contains('Jeans').click()
    cy.get('h2').contains('Men - Jeans Products').should('be.visible')
  });

  it('TC16 - Mở danh mục KIDS và chọn Dress, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.get('.left-sidebar').scrollIntoView()
    cy.get('a[data-toggle="collapse"][href="#Kids"]').click()
    cy.get('#Kids a').contains('Dress').click()
    cy.get('h2').contains('Kids - Dress Products').should('be.visible')
  });

  it('TC17 - Mở danh mục KIDS và chọn Tops & Shirts, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.get('.left-sidebar').scrollIntoView()
    cy.get('a[data-toggle="collapse"][href="#Kids"]').click()
    cy.get('#Kids a').contains('Tops & Shirts').click()
    cy.get('h2').contains('Kids - Tops & Shirts Products').should('be.visible')
  });

  it('TC18 - Mở mục Brands và chọn thương hiệu Polo, kiểm tra trang sản phẩm hiển thị đúng', () => {
    cy.contains('h2', 'Brands').scrollIntoView()
    cy.get('a[href="/brand_products/Polo"]').click()
    cy.url().should('include', '/brand_products/Polo')
  });
  
  it('TC19 - Hiển thị sản phẩm thuộc thương hiệu H&M', () => {
    cy.get('a[href="/brand_products/H&M"]').click()
    cy.url().should('include', '/brand_products/H&M')
  });

  it('TC20 - Hiển thị sản phẩm thuộc thương hiệu MADAME', () => {
    cy.get('a[href="/brand_products/Madame"]').click()
    cy.url().should('include', '/brand_products/Madame')
  });

  it('TC21 - Hiển thị sản phẩm thuộc thương hiệu MAST & HARBOUR', () => {
    cy.scrollTo('bottom')
    cy.xpath("//a[contains(@href, 'Mast') and contains(@href, 'Harbour')]").click()
    cy.url().should('include', '/brand_products/Mast')
  });

  it('TC22 - Hiển thị sản phẩm thuộc thương hiệu BABYHUG', () => {
    cy.get('a[href="/brand_products/Babyhug"]').click()
    cy.url().should('include', '/brand_products/Babyhug')
  });
  
  it('TC23 - Hiển thị sản phẩm thuộc brand ALLEN SOLLY JUNIOR', () => {
    // Cuộn xuống để phần Brands chắc chắn hiển thị
    cy.scrollTo('bottom')

    // Click vào link brand ALLEN SOLLY JUNIOR (dùng xpath)
    cy.xpath("//a[contains(@href, 'Allen') and contains(@href, 'Solly') and contains(@href, 'Junior')]").click()

    // Kiểm tra URL đúng
    cy.url().should('include', '/brand_products/Allen%20Solly%20Junior')
  });

  it('TC24 - Hiển thị sản phẩm thuộc brand KOOKIE KIDS', () => {
    // Cuộn tới phần Brands
    cy.xpath("//h2[text()='Brands']").scrollIntoView()

    // Click vào link KOOKIE KIDS
    cy.xpath("//a[@href='/brand_products/Kookie Kids']").click()

    // Kiểm tra URL đúng
    cy.url().should('include', '/brand_products/Kookie%20Kids')
  });

  it('TC25 - Hiển thị sản phẩm thuộc brand BIBA', () => {
    // Click vào link brand BIBA
    cy.xpath("//a[@href='/brand_products/Biba']").click()

    // Kiểm tra URL đúng
    cy.url().should('include', '/brand_products/Biba')
  });
  
  it('TC26 - Kiểm tra nút "View Product" hiển thị khi hover vào sản phẩm ngẫu nhiên', () => {
    cy.xpath("//h2[text()='Category' or text()='Recommended Items' or text()='Features Items']")
      .first()
      .then($el => {
        $el[0].scrollIntoView()
      })

    cy.get('.features_items .col-sm-4').then(($products) => {
      const randomIndex = Math.floor(Math.random() * $products.length)
      const chosenProduct = $products.eq(randomIndex)

      cy.wrap(chosenProduct).trigger('mouseover')

      cy.wrap(chosenProduct)
        .xpath(".//a[contains(text(),'View Product')]")
        .should('be.visible')
    })
  });

  it('TC27 - Kiểm tra tên sản phẩm ngẫu nhiên khớp giữa trang chủ và trang chi tiết', () => {
    // Cuộn xuống cuối trang để chắc chắn sản phẩm hiển thị
    cy.scrollTo('bottom')

    // Lấy danh sách sản phẩm
    cy.get('div.features_items div.product-image-wrapper').then(products => {
      // Chọn ngẫu nhiên 1 sản phẩm
      const randomIndex = Math.floor(Math.random() * products.length)
      const chosenProduct = products[randomIndex]

      // Lấy tên sản phẩm trên trang chủ
      cy.wrap(chosenProduct).find('div.productinfo p').invoke('text').then(productName => {
        productName = productName.trim()

        // Click nút View Product
        cy.wrap(chosenProduct).find('a').contains('View Product').click()

        // Chờ trang chi tiết hiện tên sản phẩm
        cy.get('div.product-information h2').should('be.visible').invoke('text').then(detailName => {
          detailName = detailName.trim()

          // So sánh tên sản phẩm
          expect(detailName).to.eq(productName)
        })
      })
    })
  });
  
  it('TC28 - Tất cả sản phẩm đều có nút "View Product"', () => {
	// Cuộn đến phần có tiêu đề cụ thể
	cy.xpath("//h2[text()='Category'] | //h2[text()='Features Items'] | //h2[text()='Recommended Items']")
		.first()
		.should('exist')
		.scrollIntoView()

	// Kiểm tra từng sản phẩm có nút View Product
	cy.get('.features_items .col-sm-4').each(($product, index) => {
		cy.wrap($product).find('a').contains('View Product').should('be.visible')
	})
  });

  it('TC29 - Kiểm tra popup Add to Cart hiển thị khi thêm sản phẩm ngẫu nhiên', () => {
    // Cuộn xuống cuối trang để sản phẩm hiển thị
    cy.scrollTo('bottom')

    // Lấy danh sách sản phẩm
    cy.get('.features_items .col-sm-4').then(products => {
      // Chọn ngẫu nhiên 1 sản phẩm
      const randomIndex = Math.floor(Math.random() * products.length)
      const chosenProduct = products[randomIndex]

      cy.wrap(chosenProduct).scrollIntoView({ block: 'center' }).trigger('mouseover')

      // Click nút Add to cart trong sản phẩm đã chọn
      cy.wrap(chosenProduct).find('a').contains('Add to cart').click()

      // Đợi popup hiện lên
      cy.get('#cartModal').should('be.visible')

      // Kiểm tra 2 nút View Cart và Continue Shopping hiển thị
      cy.get('#cartModal').within(() => {
        cy.get('a[href="/view_cart"]').should('be.visible')
        cy.contains('button', 'Continue Shopping').should('be.visible')
      })
    })
  });
  
  it('TC30 - Thêm sản phẩm ngẫu nhiên vào giỏ hàng và kiểm tra giỏ hàng', () => {
    cy.scrollTo(0, '50%')

    cy.get('.features_items .col-sm-4').then(products => {
      const randomIndex = Math.floor(Math.random() * products.length)
      const product = products[randomIndex]

      cy.wrap(product).scrollIntoView()

      // Lấy tên và giá sản phẩm từ .productinfo
      cy.wrap(product).find('.productinfo p').invoke('text').then(productNameText => {
        const trimmedName = productNameText.trim()

        cy.wrap(product).find('.productinfo h2').invoke('text').then(productPriceText => {
          const trimmedPrice = productPriceText.trim()

          // Click nút Add to cart trong .productinfo
          cy.wrap(product).find('.productinfo a.add-to-cart').first().click({ force: true })

          // Chờ popup hiện, click View Cart
          cy.get('#cartModal').should('be.visible')
          cy.get('#cartModal').contains('View Cart').click()

          // So sánh tên sản phẩm trong giỏ hàng lấy từ link trong .cart_description
          cy.get('.cart_description a[href*="/product_details"]').invoke('text').then(cartProductName => {
            expect(cartProductName.trim()).to.eq(trimmedName)
          })

          // So sánh giá sản phẩm trong giỏ hàng
          cy.get('.cart_price').invoke('text').then(cartProductPrice => {
            expect(cartProductPrice.trim()).to.eq(trimmedPrice)
          })

          // Kiểm tra số lượng = 1
          cy.get('.cart_quantity button').invoke('text').then(text => {
			expect(text.trim()).to.eq('1')
		  })
        })
      })
    })
  });

  it('TC31 - Đóng popup Continue Shopping và kiểm tra không chuyển trang', () => {
    cy.get('.product-image-wrapper').then($products => {
      const randomIndex = Math.floor(Math.random() * $products.length)
      const product = $products.eq(randomIndex)

    cy.wrap(product)
      .scrollIntoView()
      .trigger('mouseover')

    cy.wrap(product)
      .find('a.add-to-cart')
      .first()   // <-- sửa ở đây
      .click({ force: true })

    cy.get('#cartModal').should('be.visible')

    cy.get('#cartModal').within(() => {
      cy.contains('button', 'Continue Shopping').click()
    })

    cy.get('#cartModal').should('not.be.visible')
    cy.url().should('include', 'automationexercise.com')
    })
  });

});

