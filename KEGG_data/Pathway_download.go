package main

import (
    "os"
    "fmt"
    "log"
    "io/ioutil"
    "strings"
    "time"
    "sync"
    "compress/gzip"
    "net/http"
)

const url = "http://www.kegg.jp/kegg-bin/download_htext?htext=%s&format=htext&filedir="

func main() {
    if len(os.Args) == 1 || os.Args[1] == "-h" || os.Args[1] == "--help"{
        fmt.Println("Get KEGG pathway keg file by provide organism code(s), e.g. hsa mmu.")
        fmt.Println("\nproject: https://github.com/d2jvkpn/BioinformaticsAnalysis")
        return
    }

    num := 10
    if num > len (os.Args) - 1 {num = len(os.Args) - 1}
    ch := make(chan bool, num)

    var wg sync.WaitGroup

    for _, v := range(os.Args[1:]) {
        ch <- true
        wg.Add (1)

        go func (p string) {
            defer func() { <- ch }()
            defer wg.Done()
            log.Printf ("%s  Quering %s...\n", time.Now().Format("-0700"), p)

            resp, err := http.Get (fmt.Sprintf(url, p))
            if err != nil { log.Println (err); return }
            defer resp.Body.Close()

            body, err := ioutil.ReadAll(resp.Body)
            if err != nil { log.Println (err); return }
            lines := strings.Split (string(body), "\n")

            b := strings.HasPrefix(lines[len(lines)-2], "#Last updated:")
            if ! b {
                log.Printf ("%s  Failed to get %s\n", time.Now().Format("-0700"), p)
                return
            }

            file, err := os.Create(p + ".gz")
            if err != nil { log.Println(err); return }
            defer file.Close()

            gw := gzip.NewWriter(file)
            gw.Write (body)
            gw.Close()

            log.Printf ("%s  Saved %s...\n", time.Now().Format("-0700"), p)

        } (v + "00001.keg")
    }

    wg.Wait()
}
