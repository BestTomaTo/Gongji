import { By, Builder, Browser, until } from "selenium-webdriver";
import chrome from "selenium-webdriver";

let pageNum = 0;
try {
  // URL 연결
  let driver = await new Builder().forBrowser(Browser.CHROME).build();
  await driver.get(
    "https://www.hongik.ac.kr/kr/education/notice-undergrad.do?mode=list&srCategoryId=&srStartDt=&srEndDt=&srSearchKey=article_title&srSearchVal="
  );

  // Page 분류
  for (let page = 1; page < 6; page++) {
    console.log(`page : ${page}`);

    // 목차 변경
    if (page == 3) pageNum = page + 2; // page >= 3일 경우 DOM 변경되는 거 적용
    let button_xpath = `//*[@id="cms-content"]/div/div/div[2]/div[3]/div/ul/li[${
      page >= 3 ? pageNum : page
    }]/a`;
    const nextButton = await driver.findElement(By.xpath(button_xpath));

    // button이 나올때까지 명시적 대기
    await driver.wait(until.elementIsVisible(nextButton), 10000);
    await driver.wait(until.elementIsEnabled(nextButton), 10000);
    await nextButton.click();

    // 스크래핑
    for (let x = 1; x <= 10; x++) {
      let list_xpath = `//*[@id="cms-content"]/div/div/div[2]/div[2]/table/tbody/tr[${x}]/td[2]/div/a`;
      let date_xpath = `//*[@id="cms-content"]/div/div/div[2]/div[2]/table/tbody/tr[8]/td[4]`;
      const list = await driver.findElement(By.xpath(list_xpath)); // 리스트
      const date = await driver.findElement(By.xpath(date_xpath)); // 날짜
      console.log(await list.getText(), await date.getText());
      console.log(await source.getAttribute("href")); // URL
    }
    pageNum++;
  }

  // 드라이버 종료
  driver.quit();
} catch (e) {
  console.log(e);
}
