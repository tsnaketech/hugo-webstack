# Hugo Webstack Theme

This project is based on the purely static URL navigation website webstack.cc theme produced by the Hugo . It is a static responsive URL navigation theme based on Hugo. <br/>

## Theme demo address

  - Site: https://nav.snaketech.net
  - Source code: https://github.com/tsnaketech/navigation

## Feature

This is the Hugo version of the WebStack theme. You can use the following platform to host and deploy directly without a server. 

- [Webify](https://webify.cloudbase.net/) | [Netlify](https://app.netlify.com/) | [Cloudflare Pages](https://pages.cloudflare.com) | [Vercel](https://vercel.com) | [Github Pages](https://pages.github.com/)

Characteristics general:

- The all-time favorite Hugo deployment method is adopted, which is convenient and efficient. 
- The main configuration information is integrated into `config/_default/config.yaml`, complete various customized configurations with one click. 
- All navigation information is integrated in `data/webstack.yml` file to facilitate subsequent additions, deletions, and changes.
  
```yaml
- taxonomy: Favories
  icon: far fa-star
  links:

    - title: Creative Fabrica
      url: https://www.creativefabrica.com/
      logo: creativefabrica.ico
      description: Creative Fabrica is created in Amsterdam, one of the most inspirational cities in the world.

    - title: GitHub Explore
      url: https://github.com/explore
      logo: github.svg
      description: GitHub open source community.
```
- Made mobile computer adaptive and night mode.
- ~~Added search function and drop-down hot word options (based on Baidu API).~~
- Added Yiyan and Zefeng weather APIs. 

## Feature added
- Font Awesome updated to version 6 free.
- Using search items in a **yaml** file.
- Using sidebar menu items in a **yaml** file.
- Additional navigation using the `nav` directory in `content` and `data`.

### Add a new navigation

Create directories and files in the `content/nav` directory. The directory name is the navigation name, and the file name is the navigation name. For exemple `content/nav/programming.md`.

```markdown
---

title: Programming
search: true
url: /programming
type: nav
file: programming

---
```

And add the navigation items in the `data/nav/programming.yml` file.

```yaml
---
- taxonomy: Programming
  icon: fas fa-code
  links:
    - title: SnakeTech
      url: https://github.com/tsnaketech
      logo: snaketech.ico
      description: SnakeTech GitHub account.
---
```

One last thing, add in `data/header.yml` file the new navigation.

```yaml
  - name : Programming
    icon: fas fa-code fa-lg
    link: /programming
```

## Instructions for use

This is an open source public project. You can use it to make your own website navigation, or you can make websites that have nothing to do with navigation.

WebStack has many modified versions, and this is one of them. If you have made some personalized adjustments to this theme, please the [issue](https://github.com/shenweiyan/WebStack-Hugo/issues) in this project share it in.

If you want to search for icons, you'll find them at [Font Awesome](https://fontawesome.com/search?o=r&m=free).

## Grateful  

Part of the code in this topic refers to the following open source projects, thank you very much. 

- [WebStackPage/WebStackPage.github.io](https://github.com/WebStackPage/WebStackPage.github.io)
- [liutongxu/liutongxu.github.io](https://github.com/liutongxu/liutongxu.github.io)
- [iplaycode/webstack-hugo](https://github.com/iplaycode/webstack-hugo)
- [shenweiyan/WebStack-Hugo](https://github.com/shenweiyan/WebStack-Hugo)

## To Do

- Change logo.
- Favorites management with an additional yaml entry.
- Review the SEO section.
- Change weather api.
- Adapting headers for the mobile version.